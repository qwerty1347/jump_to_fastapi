from fastapi import APIRouter

from common.constants.route import RouteConstants
from common.utils.router import auto_include_domain_routers


api_v1_router = APIRouter(prefix=RouteConstants.API_V1_PREFIX)

auto_include_domain_routers(api_v1_router, router_module_paths=["routers.v1.router"])