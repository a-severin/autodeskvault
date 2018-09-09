from zeep import Client
import types
from enum import Enum


class Vault(object):
    def __init__(self, host: str, vault_name: str, user: str, password: str):
        response = Client(
            'http://pointvault.pointcad.ru/AutodeskDM/Services/Filestore/v24/AuthService.svc?singleWsdl').service.SignIn(
            host, user, password, vault_name)
        header = response['header']
        client = Client(
            'http://pointvault.pointcad.ru/AutodeskDM/Services/Filestore/v24/AuthService.svc?singleWsdl')
        client.set_default_soapheaders([header])
        self.auauth_service = client.service

        client = Client(
            'http://pointvault.pointcad.ru/AutodeskDM/Services/v24/CustomEntityService.svc?singleWsdl')
        client.set_default_soapheaders([header])
        self.custom_entity_service = client.service

        client = Client(
            'http://pointvault.pointcad.ru/AutodeskDM/Services/v24/PropertyService.svc?singleWsdl')
        client.set_default_soapheaders([header])
        self.property_service = client.service

        client = Client('http://pointvault.pointcad.ru/AutodeskDM/Services/v24/DocumentService.svc?singleWsdl')
        client.set_default_soapheaders([header])
        self.document_service = client.service


class EntityClassId(Enum):
    Files = "FILE"
    Items = "ITEM"
    ChangeOrders = "CO"
    ForumMessage = "FRMMSG"
    ItemReferenceDesignators = "ITEMRDES"
    Folder = "FLDR"
    Link = "LINK"
    CustomObject = "CUSTENT"
    Root = "ROOT"


class ClientProperties(Enum):
    EntityClass = "EntityType"
    EntityClassID = "EntityTypeID"
    EntityIcon = "EntityIcon"
    EntityPath = "EntityPath"
    FullPath = "FullPath"
    EntityDescription = "EntityDescription"
    LinkTargetPath = "LinkTargetPath"
    FolderCreateDate = "Folder!CreateDate"
    HasAttachments = "Entity!HasAttachments"
    VaultStatus = "File!VaultStatus"
    VaultStatusModifier = "File!VaultStatusModifier"


class ServerProperties(Enum):
    EntityName = "Name"
    NumAttachments = "NumManualAttachments"
    CONumFileAttachments = "NumFileAttachments"
    CategoryGlyph = "CategoryGlyph"
    CategoryGlyphVer = "CategoryGlyph(Ver)"
    CategoryName = "CategoryName"
    CategoryNameVer = "CategoryName(Ver)"
    FileName = "ClientFileName"
    FileStatus = "Status"
    VisualizationAttachment = "VisualizationAttachment"
    VisualizationCompliance = "VisualizationCompliance"
    FileCompliance = "Compliance"
    FileComplianceVer = "Compliance(Ver)"
    LatestVersion = "LatestVersion"
    ReleasedRevision = "ReleasedRevision"
    LatestReleasedRevision = "LatestReleasedRevision"
    ThumbnailSystem = "Thumbnail"
    ControlledByCO = "ControlledByChangeOrder"
    ChangeOrderState = "ChangeOrderState"
    Title = "Title"
    TitleItemCO = "Title(Item,CO)"
    Description = "Description"
    CreateUserName = "CreateUserName"
    VersionNumber = "VersionNumber"
    Comment = "Comment"
    CheckInDate = "CheckInDate"
    ModifiedDate = "ModDate"
    ItemLinked = "ItemLinked"
    ItemAssignable = "ItemAssignable"
    Author = "Author"
    Keywords = "Keywords"
    Hidden = "Hidden"
    Classification = "Classification"
    LifeCycleState = "State"
    LifeCycleDefinitionVersion = "LifeCycleDefinition(Ver)"
    LifeCycleDefinition = "LifeCycleDefinition"
    LifeCycleStateVersion = "State(Ver)"
    Revision = "Revision"
    CheckOutUserName = "CheckoutUserName"
    CheckOutLocalSpec = "CheckoutLocalSpec"
    ReplicationLeasedUntil = "ReplicationLeasedUntil"
    ReplicationCurrentOwner = "ReplicationCurrentOwner"
    FileReplicated = "FileReplicated"
    ILogicRuleStatus = "iLogicRuleStatus"
    Obsolete = "Obsolete"
    FileSize = "FileSize"
    FolderPath = "FolderPath"
    ItemNumber = "Number"
    ItemEffectivity = "ItemEffectivity"
    ItemEquivalence = "Equivalence"
    ItemTitle = "Title(Item,CO)"
    ItemDescription = "Description(Item,CO)"
    ItemUnits = "Units"
    ItemEffectivityStartDate = "ItemEffectivityStart"
    ItemEffectivityEndDate = "ItemEffectivityEnd"
    ItemFileLinkState = "FileLinkState"
    ChangeOrderReviewStatus = "ReviewStatus"


class SearchOperation(Enum):
    # <summary>
    # Valid on property types: string
    # SearchText needed: yes
    # </summary>
    Contains = 1

    # <summary>
    # Valid on property types: string
    # SearchText needed: yes
    # </summary>
    DoesNotContain = 2

    # <summary>
    # Valid on property types: numeric, bool, datetime, string
    # SearchText needed: yes
    # </summary>
    IsExactlyOrEquals = 3

    # <summary>
    # Valid on property types: image, string
    # SearchText needed: no
    # </summary>
    IsEmpty = 4

    # <summary>
    # Valid on property types: image, string
    # SearchText needed: no
    # </summary>
    IsNotEmpty = 5

    # <summary>
    # Valid on property types: numeric, datetime, string
    # SearchText needed: yes
    # </summary>
    GreaterThan = 6

    # <summary>
    # Valid on property types: numeric, datetime, string
    # SearchText needed: yes
    # </summary>
    GreaterThanOrEqualTo = 7

    # <summary>
    # Valid on property types: numeric, datetime, string
    # SearchText needed: yes
    # </summary>
    LessThan = 8

    # <summary>
    # Valid on property types: numeric, datetime, string
    # SearchText needed: yes
    # </summary>
    LessThanOrEqualTo = 9

    # <summary>
    # Valid on property types: numeric, bool, string
    # SearchText needed: yes
    # </summary>
    NotEqualTo = 10


class PropertySearch(Enum):
    SingleProperty = "SingleProperty"
    AllProperties = "AllProperties"
    AllPropertiesAndContent = "AllPropertiesAndContent"


class SearchRule(Enum):
    Must = "Must"
    May = "May"
    MustNot = "MustNot"
