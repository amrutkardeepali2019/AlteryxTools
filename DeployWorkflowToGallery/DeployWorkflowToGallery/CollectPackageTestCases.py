import os


absroot = os.path.abspath("TestCases")

single_absolute_macro = """<?xml version="1.0"?>
<AlteryxDocument yxmdVer="2019.1">
  <Nodes>
    <Node ToolID="1">
      <GuiSettings Plugin="AlteryxBasePluginsGui.TextInput.TextInput">
        <Position x="102" y="78" />
      </GuiSettings>
      <Properties>
        <Configuration>
          <NumRows value="1" />
          <Fields>
            <Field name="Field1" />
          </Fields>
          <Data>
            <r>
              <c>A</c>
            </r>
          </Data>
        </Configuration>
        <Annotation DisplayMode="0">
          <Name />
          <DefaultAnnotationText />
          <Left value="False" />
        </Annotation>
      </Properties>
      <EngineSettings EngineDll="AlteryxBasePluginsEngine.dll" EngineDllEntryPoint="AlteryxTextInput" />
    </Node>
    <Node ToolID="3">
      <GuiSettings Plugin="AlteryxBasePluginsGui.BrowseV2.BrowseV2">
        <Position x="294" y="78" />
      </GuiSettings>
      <Properties>
        <Configuration />
        <Annotation DisplayMode="0">
          <Name />
          <DefaultAnnotationText />
          <Left value="False" />
        </Annotation>
      </Properties>
      <EngineSettings EngineDll="AlteryxBasePluginsEngine.dll" EngineDllEntryPoint="AlteryxBrowseV2" />
    </Node>
    <Node ToolID="4">
      <GuiSettings>
        <Position x="198" y="78" />
      </GuiSettings>
      <Properties>
        <Configuration />
        <Annotation DisplayMode="0">
          <Name>Macro (2)</Name>
          <DefaultAnnotationText />
          <Left value="False" />
        </Annotation>
      </Properties>
      <EngineSettings Macro="{0}\Macro.yxmc" />
    </Node>
  </Nodes>
  <Connections>
    <Connection>
      <Origin ToolID="1" Connection="Output" />
      <Destination ToolID="4" Connection="Input2" />
    </Connection>
    <Connection>
      <Origin ToolID="4" Connection="Output3" />
      <Destination ToolID="3" Connection="Input" />
    </Connection>
  </Connections>
  <Properties>
    <Memory default="True" />
    <GlobalRecordLimit value="0" />
    <TempFiles default="True" />
    <Annotation on="True" includeToolName="False" />
    <ConvErrorLimit value="10" />
    <ConvErrorLimit_Stop value="False" />
    <CancelOnError value="False" />
    <DisableBrowse value="False" />
    <EnablePerformanceProfiling value="False" />
    <DisableAllOutput value="False" />
    <ShowAllMacroMessages value="False" />
    <ShowConnectionStatusIsOn value="True" />
    <ShowConnectionStatusOnlyWhenRunning value="True" />
    <ZoomLevel value="0" />
    <LayoutType>Horizontal</LayoutType>
    <MetaInfo>
      <NameIsFileName value="True" />
      <Name>Test</Name>
      <Description />
      <RootToolName />
      <ToolVersion />
      <ToolInDb value="False" />
      <CategoryName />
      <SearchTags />
      <Author />
      <Company />
      <Copyright />
      <DescriptionLink actual="" displayed="" />
      <Example>
        <Description />
        <File />
      </Example>
    </MetaInfo>
    <Events>
      <Enabled value="True" />
    </Events>
  </Properties>
</AlteryxDocument>""".format(absroot)

single_absolute_macro_container = """<?xml version="1.0"?>
<AlteryxDocument yxmdVer="2019.1">
  <Nodes>
    <Node ToolID="1">
      <GuiSettings Plugin="AlteryxBasePluginsGui.TextInput.TextInput">
        <Position x="126" y="138" />
      </GuiSettings>
      <Properties>
        <Configuration>
          <NumRows value="1" />
          <Fields>
            <Field name="Field1" />
          </Fields>
          <Data>
            <r>
              <c>A</c>
            </r>
          </Data>
        </Configuration>
        <Annotation DisplayMode="0">
          <Name />
          <DefaultAnnotationText />
          <Left value="False" />
        </Annotation>
      </Properties>
      <EngineSettings EngineDll="AlteryxBasePluginsEngine.dll" EngineDllEntryPoint="AlteryxTextInput" />
    </Node>
    <Node ToolID="4">
      <GuiSettings Plugin="AlteryxBasePluginsGui.BrowseV2.BrowseV2">
        <Position x="390" y="138" />
      </GuiSettings>
      <Properties>
        <Configuration>
          <Layout>
            <View1>
              <Hints>
                <Table />
              </Hints>
            </View1>
          </Layout>
        </Configuration>
        <Annotation DisplayMode="0">
          <Name />
          <DefaultAnnotationText />
          <Left value="False" />
        </Annotation>
      </Properties>
      <EngineSettings EngineDll="AlteryxBasePluginsEngine.dll" EngineDllEntryPoint="AlteryxBrowseV2" />
    </Node>
    <Node ToolID="2">
      <GuiSettings Plugin="AlteryxGuiToolkit.ToolContainer.ToolContainer">
        <Position x="210" y="102" width="145.3507" height="133" />
      </GuiSettings>
      <Properties>
        <Configuration>
          <Caption>Container 2</Caption>
          <Style TextColor="#314c4a" FillColor="#ecf2f2" BorderColor="#314c4a" Transparency="25" Margin="25" />
          <Disabled value="False" />
          <Folded value="False" />
        </Configuration>
        <Annotation DisplayMode="0">
          <Name />
          <DefaultAnnotationText />
          <Left value="False" />
        </Annotation>
      </Properties>
      <ChildNodes>
        <Node ToolID="3">
          <GuiSettings>
            <Position x="235" y="151" />
          </GuiSettings>
          <Properties>
            <Configuration />
            <Annotation DisplayMode="0">
              <Name />
              <DefaultAnnotationText />
              <Left value="False" />
            </Annotation>
            <Dependencies>
              <Implicit />
            </Dependencies>
          </Properties>
          <EngineSettings Macro="{0}\Macro.yxmc" />
        </Node>
      </ChildNodes>
    </Node>
  </Nodes>
  <Connections>
    <Connection>
      <Origin ToolID="1" Connection="Output" />
      <Destination ToolID="3" Connection="Input2" />
    </Connection>
    <Connection>
      <Origin ToolID="3" Connection="Output3" />
      <Destination ToolID="4" Connection="Input" />
    </Connection>
  </Connections>
  <Properties>
    <Memory default="True" />
    <GlobalRecordLimit value="0" />
    <TempFiles default="True" />
    <Annotation on="True" includeToolName="False" />
    <ConvErrorLimit value="10" />
    <ConvErrorLimit_Stop value="False" />
    <CancelOnError value="False" />
    <DisableBrowse value="False" />
    <EnablePerformanceProfiling value="False" />
    <DisableAllOutput value="False" />
    <ShowAllMacroMessages value="False" />
    <ShowConnectionStatusIsOn value="True" />
    <ShowConnectionStatusOnlyWhenRunning value="True" />
    <ZoomLevel value="0" />
    <LayoutType>Horizontal</LayoutType>
    <MetaInfo>
      <NameIsFileName value="True" />
      <Name>Test2</Name>
      <Description />
      <RootToolName />
      <ToolVersion />
      <ToolInDb value="False" />
      <CategoryName />
      <SearchTags />
      <Author />
      <Company />
      <Copyright />
      <DescriptionLink actual="" displayed="" />
      <Example>
        <Description />
        <File />
      </Example>
    </MetaInfo>
    <Events>
      <Enabled value="True" />
    </Events>
  </Properties>
</AlteryxDocument>""".format(absroot)

single_absolute_macro_invalid = """<?xml version="1.0"?>
<AlteryxDocument yxmdVer="2019.1">
  <Nodes>
    <Node ToolID="1">
      <GuiSettings Plugin="AlteryxBasePluginsGui.TextInput.TextInput">
        <Position x="102" y="78" />
      </GuiSettings>
      <Properties>
        <Configuration>
          <NumRows value="1" />
          <Fields>
            <Field name="Field1" />
          </Fields>
          <Data>
            <r>
              <c>A</c>
            </r>
          </Data>
        </Configuration>
        <Annotation DisplayMode="0">
          <Name />
          <DefaultAnnotationText />
          <Left value="False" />
        </Annotation>
      </Properties>
      <EngineSettings EngineDll="AlteryxBasePluginsEngine.dll" EngineDllEntryPoint="AlteryxTextInput" />
    </Node>
    <Node ToolID="3">
      <GuiSettings Plugin="AlteryxBasePluginsGui.BrowseV2.BrowseV2">
        <Position x="294" y="78" />
      </GuiSettings>
      <Properties>
        <Configuration />
        <Annotation DisplayMode="0">
          <Name />
          <DefaultAnnotationText />
          <Left value="False" />
        </Annotation>
      </Properties>
      <EngineSettings EngineDll="AlteryxBasePluginsEngine.dll" EngineDllEntryPoint="AlteryxBrowseV2" />
    </Node>
    <Node ToolID="4">
      <GuiSettings>
        <Position x="198" y="78" />
      </GuiSettings>
      <Properties>
        <Configuration />
        <Annotation DisplayMode="0">
          <Name>Macro (2)</Name>
          <DefaultAnnotationText />
          <Left value="False" />
        </Annotation>
      </Properties>
      <EngineSettings Macro="{0}\InvalidMacro.yxmc" />
    </Node>
  </Nodes>
  <Connections>
    <Connection>
      <Origin ToolID="1" Connection="Output" />
      <Destination ToolID="4" Connection="Input2" />
    </Connection>
    <Connection>
      <Origin ToolID="4" Connection="Output3" />
      <Destination ToolID="3" Connection="Input" />
    </Connection>
  </Connections>
  <Properties>
    <Memory default="True" />
    <GlobalRecordLimit value="0" />
    <TempFiles default="True" />
    <Annotation on="True" includeToolName="False" />
    <ConvErrorLimit value="10" />
    <ConvErrorLimit_Stop value="False" />
    <CancelOnError value="False" />
    <DisableBrowse value="False" />
    <EnablePerformanceProfiling value="False" />
    <DisableAllOutput value="False" />
    <ShowAllMacroMessages value="False" />
    <ShowConnectionStatusIsOn value="True" />
    <ShowConnectionStatusOnlyWhenRunning value="True" />
    <ZoomLevel value="0" />
    <LayoutType>Horizontal</LayoutType>
    <MetaInfo>
      <NameIsFileName value="True" />
      <Name>Test</Name>
      <Description />
      <RootToolName />
      <ToolVersion />
      <ToolInDb value="False" />
      <CategoryName />
      <SearchTags />
      <Author />
      <Company />
      <Copyright />
      <DescriptionLink actual="" displayed="" />
      <Example>
        <Description />
        <File />
      </Example>
    </MetaInfo>
    <Events>
      <Enabled value="True" />
    </Events>
  </Properties>
</AlteryxDocument>""".format(absroot)
