# generated by datamodel-codegen:
#   filename:  definitions.json
#   timestamp: 2023-07-19T18:11:15+00:00

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional, Union
from uuid import UUID

from pydantic import BaseModel, Extra, Field, constr


class DurableId(BaseModel):
    class Config:
        allow_population_by_field_name = True

    __root__: constr(regex=r'^[a-z](-?[a-z0-9]+)*/[a-z0-9-]+(\/?[a-z0-9-])*$')
    """
    A durable-id to an existing resource.
    """


class ExternalId(BaseModel):
    class Config:
        allow_population_by_field_name = True

    external_id: constr(
        regex=r'^[a-z0-9][a-z0-9-_]{2,49}$', min_length=3, max_length=50
    ) = Field(..., alias='externalId')
    """
    ExternalId for product and plan references. Property reference must be named product or plan.
    """


class ResourceName(BaseModel):
    class Config:
        allow_population_by_field_name = True

    resource_name: constr(
        regex=r'^[a-zA-Z0-9-_]+$', min_length=1, max_length=50
    ) = Field(..., alias='resourceName')
    """
    Resource Name that can be referenced using this value by another resource.
    """


class ResourceReference(BaseModel):
    class Config:
        allow_population_by_field_name = True

    __root__: Union[DurableId, ExternalId, ResourceName]


class ResourceLifecycleState(Enum):
    not_available = 'notAvailable'
    never_used = 'neverUsed'
    test = 'test'
    preview = 'preview'
    generally_available = 'generallyAvailable'
    deprecated = 'deprecated'
    decommissioned = 'decommissioned'
    deleted = 'deleted'


class Reason(Enum):
    critical_security_issue = 'criticalSecurityIssue'
    end_of_support = 'endOfSupport'
    other = 'other'


class ProductReference(BaseModel):
    class Config:
        extra = Extra.forbid
        allow_population_by_field_name = True

    product: ResourceReference


class PlanReference(BaseModel):
    class Config:
        extra = Extra.forbid
        allow_population_by_field_name = True

    plan: ResourceReference


class Level(Enum):
    informational = 'informational'
    warning = 'warning'


class ProductIngestionSchemaUri(BaseModel):
    class Config:
        allow_population_by_field_name = True

    __root__: constr(
        regex=r'^https://(schema(-int)?\.mp\.microsoft\.com)|(product-ingestion(-int)?\.azureedge\.net)/schema/[a-z][a-z0-9]+(?:-[a-z0-9]+)*/\d{4}(?:-\d\d){2}(?:-dev|-preview\d+)?$'
    ) = Field(..., title='Product Ingestion schema uri')


class Code(Enum):
    business_validation_error = 'businessValidationError'
    collection_limit_exceeded = 'collectionLimitExceeded'
    invalid_id = 'invalidId'
    invalid_entity_status = 'invalidEntityStatus'
    invalid_request = 'invalidRequest'
    invalid_resource = 'invalidResource'
    invalid_state = 'invalidState'
    not_deployed = 'notDeployed'
    not_supported = 'notSupported'
    operation_canceled = 'operationCanceled'
    product_locked = 'productLocked'
    resource_not_found = 'resourceNotFound'
    schema_validation_error = 'schemaValidationError'


class InnerError(BaseModel):
    class Config:
        allow_population_by_field_name = True

    resource_id: Optional[ResourceReference] = Field(None, alias='resourceId')
    code: Code
    message: Optional[str] = None
    details: Optional[list[InnerError]] = None


class Identity(BaseModel):
    class Config:
        allow_population_by_field_name = True

    external_id: constr(
        regex=r'^[a-z0-9][a-z0-9-_]{2,49}$', min_length=3, max_length=50
    ) = Field(..., alias='externalId')


class LegacyXboxProductType(Enum):
    addon_extension = 'addonExtension'
    arcade = 'arcade'
    avatar = 'avatar'
    x360_disc = 'x360Disc'
    game_addon = 'gameAddon'
    gamer_tile = 'gamerTile'
    game_trailer = 'gameTrailer'
    game_video = 'gameVideo'
    theme = 'theme'
    x360_game_consumable = 'x360GameConsumable'
    xbo = 'xbo'


class Xbox360Identity(BaseModel):
    class Config:
        allow_population_by_field_name = True

    legacy_xbox_product_id: UUID = Field(..., alias='legacyXboxProductId')
    legacy_xbox_product_type: LegacyXboxProductType = Field(
        ..., alias='legacyXboxProductType'
    )
    store_id: str = Field(..., alias='storeId')
    xbox_title_id: constr(regex=r'^[1-9][0-9]{0,19}$') = Field(..., alias='xboxTitleId')


class Type(Enum):
    azure_application = 'azureApplication'
    azure_container = 'azureContainer'
    azure_virtual_machine = 'azureVirtualMachine'
    consulting_service = 'consultingService'
    container_app = 'containerApp'
    core_virtual_machine = 'coreVirtualMachine'
    cosell_only = 'cosellOnly'
    dynamics365_business_central = 'dynamics365BusinessCentral'
    dynamics365_for_customer_engagement = 'dynamics365ForCustomerEngagement'
    dynamics365_for_operations = 'dynamics365ForOperations'
    iot_edge_module = 'iotEdgeModule'
    managed_service = 'managedService'
    power_bi_app = 'powerBiApp'
    power_bi_visual = 'powerBiVisual'
    software_as_a_service = 'softwareAsAService'
    xbox360_non_backcompat = 'xbox360NonBackcompat'


class Type1(Enum):
    xbox360_non_backcompat = 'xbox360NonBackcompat'


class Product(BaseModel):
    class Config:
        allow_population_by_field_name = True

    type: Optional[Type1] = None
    identity: Optional[Xbox360Identity] = None


class Product1(BaseModel):
    pass

    class Config:
        allow_population_by_field_name = True


class Type2(Enum):
    azure_application = 'azureApplication'
    azure_container = 'azureContainer'
    azure_virtual_machine = 'azureVirtualMachine'
    consulting_service = 'consultingService'
    container_app = 'containerApp'
    core_virtual_machine = 'coreVirtualMachine'
    cosell_only = 'cosellOnly'
    dynamics365_business_central = 'dynamics365BusinessCentral'
    dynamics365_for_customer_engagement = 'dynamics365ForCustomerEngagement'
    dynamics365_for_operations = 'dynamics365ForOperations'
    iot_edge_module = 'iotEdgeModule'
    managed_service = 'managedService'
    power_bi_app = 'powerBiApp'
    power_bi_visual = 'powerBiVisual'
    software_as_a_service = 'softwareAsAService'
    xbox360_non_backcompat = 'xbox360NonBackcompat'


class DeprecationSchedule(BaseModel):
    """
    Defines a <what> schedule for a deprecated resource
    """

    class Config:
        extra = Extra.forbid
        allow_population_by_field_name = True

    field_schema: Optional[ProductIngestionSchemaUri] = Field(None, alias='$schema')
    date: Optional[date] = None
    date_offset: Optional[str] = Field(None, alias='dateOffset')
    reason: Optional[Reason] = None
    alternative: Optional[Union[ProductReference, PlanReference]] = None


class Validation(InnerError):
    class Config:
        allow_population_by_field_name = True

    field_schema: Optional[ProductIngestionSchemaUri] = Field(None, alias='$schema')
    level: Level


class Product2(Product):
    class Config:
        allow_population_by_field_name = True

    product_group: Optional[ResourceReference] = Field(None, alias='productGroup')
    identity: Identity
    type: Type2
    alias: constr(max_length=120)
    lifecycle_state: Optional[ResourceLifecycleState] = Field(
        'generallyAvailable', alias='lifecycleState'
    )
    deprecation_schedule: Optional[DeprecationSchedule] = Field(
        None, alias='deprecationSchedule'
    )


class Product3(Product1):
    class Config:
        allow_population_by_field_name = True

    product_group: Optional[ResourceReference] = Field(None, alias='productGroup')
    identity: Identity
    type: Type2
    alias: constr(max_length=120)
    lifecycle_state: Optional[ResourceLifecycleState] = Field(
        'generallyAvailable', alias='lifecycleState'
    )
    deprecation_schedule: Optional[DeprecationSchedule] = Field(
        None, alias='deprecationSchedule'
    )


class Resource(BaseModel):
    class Config:
        extra = Extra.allow
        allow_population_by_field_name = True

    resource_name: Optional[constr(min_length=1, max_length=50)] = Field(
        None, alias='resourceName'
    )
    id: Optional[DurableId] = None
    validations: Optional[list[Validation]] = None


class MicrosoftProductIngestionProductSchema(Resource):
    class Config:
        allow_population_by_field_name = True

    product_group: Optional[ResourceReference] = Field(None, alias='productGroup')
    identity: Identity
    type: Type
    alias: constr(max_length=120)
    lifecycle_state: Optional[ResourceLifecycleState] = Field(
        'generallyAvailable', alias='lifecycleState'
    )
    deprecation_schedule: Optional[DeprecationSchedule] = Field(
        None, alias='deprecationSchedule'
    )


class MicrosoftProductIngestionProductSchema1(
    Product2, MicrosoftProductIngestionProductSchema
):
    pass

    class Config:
        allow_population_by_field_name = True


class MicrosoftProductIngestionProductSchema2(
    Product3, MicrosoftProductIngestionProductSchema
):
    pass

    class Config:
        allow_population_by_field_name = True


class Product4(BaseModel):
    class Config:
        allow_population_by_field_name = True

    __root__: Union[
        MicrosoftProductIngestionProductSchema1, MicrosoftProductIngestionProductSchema2
    ] = Field(..., title='Microsoft Product Ingestion product schema')


InnerError.update_forward_refs()
