__all__ = ("router", )

from aiogram import Router
from .main_handlers import router as main_handlers_router
from .other_handlers import router as other_handler_router

router = Router(name=__name__)

router.include_routers(other_handler_router,
                       main_handlers_router)
