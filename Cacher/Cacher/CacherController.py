import AlteryxPythonSDK as Sdk
import xml.etree.ElementTree as Et
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import CacherPy.CacherCore_ctypes as Core


class AyxPlugin:
    def __init__(self, n_tool_id: int, alteryx_engine: object, output_anchor_mgr: object):
        # Default properties
        self.n_tool_id: int = n_tool_id
        self.alteryx_engine: Sdk.AlteryxEngine = alteryx_engine
        self.output_anchor_mgr: Sdk.OutputAnchorManager = output_anchor_mgr

        # Custom properties
        self.input: IncomingInterface = None
        self.output: Sdk.OutputAnchor = None
        self.max_size: int = 100000000

    def pi_init(self, str_xml: str):
        self.max_size = int(Et.fromstring(str_xml).find("maxSize").text)*1000000 if 'maxSize' in str_xml else 100000000
        self.output = self.output_anchor_mgr.get_output_anchor('Output')

    def pi_add_incoming_connection(self, str_type: str, str_name: str) -> object:
        self.input = IncomingInterface(self)
        return self.input

    def pi_add_outgoing_connection(self, str_name: str) -> bool:
        return True

    def pi_push_all_records(self, n_record_limit: int) -> bool:
        self.alteryx_engine.output_message(self.n_tool_id, Sdk.EngineMessageType.error, 'Missing Incoming Connection.')
        return False

    def pi_close(self, b_has_errors: bool):
        self.output.assert_close()

    def display_error_msg(self, msg_string: str):
        self.alteryx_engine.output_message(self.n_tool_id, Sdk.EngineMessageType.error, msg_string)

    def display_info_msg(self, msg_string: str):
        self.alteryx_engine.output_message(self.n_tool_id, Sdk.EngineMessageType.info, msg_string)


class IncomingInterface:
    def __init__(self, parent: AyxPlugin):
        # Default properties
        self.parent: AyxPlugin = parent

        # Custom properties
        self.record_creator: Sdk.RecordCreator = None
        self.record_info: Sdk.RecordInfo = None
        self.cacher: Core.Cacher = None

    def ii_init(self, record_info_in: Sdk.RecordInfo) -> bool:
        self.record_creator = record_info_in.construct_record_creator()
        self.record_info = record_info_in
        self.parent.output.init(self.record_info)
        self.cacher = Core.Cacher(self.parent.n_tool_id, self.parent.alteryx_engine, record_info_in, self.parent.max_size)
        return True

    def ii_push_record(self, in_record: Sdk.RecordRef) -> bool:
        self.cacher.push(in_record)
        return True

    def ii_update_progress(self, d_percent: float):
        # Inform the Alteryx engine of the tool's progress.
        self.parent.alteryx_engine.output_tool_progress(self.parent.n_tool_id, d_percent)

        # Inform the outgoing connections of the tool's progress.
        self.parent.output.update_progress(d_percent / 2)

    def ii_close(self):
        self.cacher.start_read()
        while self.cacher.read():
            self.parent.output.push_record(self.cacher.current_record)

        self.cacher.close()
        self.parent.output.close()