from zeep import Client
from typing import Dict
from enum import Enum


class VaultServices(Enum):
    AdminService = 'AdminService'
    AuthService = 'AuthService'
    BehaviorService = 'BehaviorService'
    CategoryService = 'CategoryService'
    ChangeOrderService = 'ChangeOrderService'
    CustomEntityService = 'CustomEntityService'
    DocumentService = 'DocumentService'
    DocumentServiceExtensions = 'DocumentServiceExtensions'
    FilestoreService = 'FilestoreService'
    FilestoreVaultService = 'FilestoreVaultService'
    ForumService = 'ForumService'
    KnowledgeVaultService = 'KnowledgeVaultService'
    InformationService = 'InformationService'
    IdentificationService = 'IdentificationService'
    ItemService = 'ItemService'
    JobService = 'JobService'
    LifeCycleService = 'LifeCycleService'
    PackageService = 'PackageService'
    PropertyService = 'PropertyService'
    ReplicationService = 'ReplicationService'
    RevisionService = 'RevisionService'
    SecurityService = 'SecurityService'


def generate_service_urls(host: str, path: str, port: int, protocol: str, version: object):
    services = {
            VaultServices.AdminService.value: f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/AdminService.svc?singleWsdl",
            VaultServices.AuthService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/Filestore/v{str(version)}/AuthService.svc?singleWsdl",
            VaultServices.BehaviorService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/BehaviorService.svc?singleWsdl",
            VaultServices.CategoryService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/CategoryService.svc?singleWsdl",
            VaultServices.ChangeOrderService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/ChangeOrderService.svc?singleWsdl",
            VaultServices.CustomEntityService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/CustomEntityService.svc?singleWsdl",
            VaultServices.DocumentService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/DocumentService.svc?singleWsdl",
            VaultServices.DocumentServiceExtensions.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/DocumentServiceExtensions.svc?singleWsdl",
            VaultServices.FilestoreService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/Filestore/v{str(version)}/FilestoreService.svc?singleWsdl",
            VaultServices.FilestoreVaultService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/Filestore/v{str(version)}/FilestoreVaultService.svc?singleWsdl",
            VaultServices.ForumService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/ForumService.svc?singleWsdl",
            VaultServices.KnowledgeVaultService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/KnowledgeVaultService.svc?singleWsdl",
            VaultServices.InformationService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/InformationService.svc?singleWsdl",
            VaultServices.IdentificationService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/Filestore/v{str(version)}/IdentificationService.svc?singleWsdl",
            VaultServices.ItemService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/ItemService.svc?singleWsdl",
            VaultServices.JobService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/JobService.svc?singleWsdl",
            VaultServices.LifeCycleService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/LifeCycleService.svc?singleWsdl",
            VaultServices.PackageService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/PackageService.svc?singleWsdl",
            VaultServices.PropertyService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/PropertyService.svc?singleWsdl",
            VaultServices.ReplicationService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/ReplicationService.svc?singleWsdl",
            VaultServices.SecurityService.value:  f"{protocol}://{host}{'' if port is None else ':' + str(port)}/{path}/AutodeskDM/Services/v{str(version)}/SecurityService.svc?singleWsdl",
        }
    return services


def connect(host: str, vault_name: str, user: str, password: str, port=None, additional_path='', protocol='http', version='24'):
    services = generate_service_urls(host, additional_path, port, protocol, version)
    response = Client(services[VaultServices.AuthService.value]).service.SignIn(host, user, password, vault_name)
    soap_header = response['header']
    return Vault(services, soap_header)


class Vault(object):
    def __init__(self, services: Dict, soap_header):
        client = Client(services[VaultServices.AuthService.value])
        client.set_default_soapheaders([soap_header])
        self.auauth_service = client.service

        client = Client(services[VaultServices.CustomEntityService.value])
        client.set_default_soapheaders([soap_header])
        self.custom_entity_service = client.service

        client = Client(services[VaultServices.PropertyService.value])
        client.set_default_soapheaders([soap_header])
        self.property_service = client.service

        client = Client(services[VaultServices.DocumentService.value])
        client.set_default_soapheaders([soap_header])
        self.document_service = client.service

        client = Client(services[VaultServices.SecurityService.value])
        client.set_default_soapheaders([soap_header])
        self.security_service = client.service

        self.UserId = soap_header['SecurityHeader']['UserId']


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

class SysAclBeh(Enum):
    '''
    System ACL is Combined - effective security is the combination of the user ACL and the system (State) ACL</summary> 
    System ACL is Override - effective security is the Override ACL
    '''
    Override = "Override"
    Combined = "Combined"