import importlib
import pkgutil

from fastapi import APIRouter


def auto_include_domain_routers(parent_router: APIRouter, base_package: str = "app.domain", router_module_paths: list[str] = None, router_attr: str = "router"):
    """
    주어진 부모 APIRouter에 도메인 라우터를 자동으로 포함시키는 함수

    매개변수:
    - parent_router (APIRouter): 포함시킬 부모 APIRouter 객체
    - base_package (str): 도메인 라우터를 검색할 기본 패키지 경로 (기본값: "app.domain")
    - router_module_paths (list[str]): 포함시킬 라우터 모듈 경로 목록
    - router_attr (str): 라우터 객체를 나타내는 모듈 내 속성 이름 (기본값: "router")
    """
    package = importlib.import_module(base_package)
    if not hasattr(package, "__path__"):
        return

    for finder, name, ispkg in pkgutil.iter_modules(package.__path__):
        domain_module_name = f"{base_package}.{name}"

        for router_path in router_module_paths:
            router_module_name = f"{domain_module_name}.{router_path}"

            try:
                mod = importlib.import_module(router_module_name)
                router = getattr(mod, router_attr)
                print(f"Including router from {router_module_name}")
                parent_router.include_router(router)

            except ModuleNotFoundError:
                continue

            except AttributeError:
                continue