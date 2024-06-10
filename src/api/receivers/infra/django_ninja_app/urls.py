import uuid

import anydi
from django.http import HttpResponse
from ninja import NinjaAPI, Query
from ninja.pagination import paginate, PageNumberPagination

from api.receivers.application.dtos import CreateReceiverIn, \
    CreateReceiverOut, ReceiverOut, ReceiverListOut, Error4xxOut, \
    DeleteReceiversIn, DeleteReceiverOut, UpdateReceiverIn, UpdateReceiverOut
from api.receivers.application.services import ReceiverService
from api.receivers.domain.repositories import ReceiverSearchParams
from api.receivers.infra.django_ninja_app.repositories import \
    AlreadyRegisteredReceiver, NotFoundException

api = NinjaAPI()


@api.post("/receivers/delete-multiple", response=DeleteReceiverOut)
def bulk_delete_receivers(
        request,
        payload: DeleteReceiversIn,
        receiver_service: ReceiverService = anydi.auto
):
    return receiver_service.delete(payload)


@api.post("/receivers", response={201: CreateReceiverOut, 400: Error4xxOut})
def create_receiver(
        request,
        payload: CreateReceiverIn,
        receiver_service: ReceiverService = anydi.auto
):
    try:
        return 201, receiver_service.create(payload)
    except AlreadyRegisteredReceiver:
        return 400, Error4xxOut(message="CPF/CNPJ já registrado")


@api.patch("/receivers/{receiver_id}", response=UpdateReceiverOut)
def update_receiver(
        request,
        receiver_id: uuid.UUID,
        payload: UpdateReceiverIn,
        receiver_service: ReceiverService = anydi.auto
):
    try:
        return receiver_service.update(receiver_id, payload)
    except NotFoundException:
        return HttpResponse("Not Found", status=404)


@api.get("/receivers/{receiver_id}", response=ReceiverOut)
def read_receiver(
        request,
        receiver_id: uuid.UUID,
        receiver_service: ReceiverService = anydi.auto
):
    try:
        return receiver_service.get(receiver_id)
    except NotFoundException:
        return HttpResponse("Not Found", status=404)


@api.get("/receivers", response=ReceiverListOut)
def list_receivers(
        request,
        filters: ReceiverSearchParams = Query(...),
        receiver_service: ReceiverService = anydi.auto
):
    receivers, items_count = receiver_service.list(filters)
    return ReceiverListOut(
        page=filters.page,
        page_size=filters.page_size,
        items_count=items_count,
        results=receivers
    )


@api.patch("/receivers/{receiver_id}", response=UpdateReceiverOut)
def update_receiver(
        request,
        receiver_id: uuid.UUID,
        payload: UpdateReceiverIn,
        receiver_service: ReceiverService = anydi.auto
):
    try:
        return receiver_service.update(receiver_id, payload)
    except NotFoundException:
        return HttpResponse("Not Found", status=404)
