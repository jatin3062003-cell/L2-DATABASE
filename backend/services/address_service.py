from repository.address_repository import (
    get_all_addresses,
    get_address,
    get_customer_addresses,
    create_address,
    update_address,
    delete_address,
)


def fetch_all_addresses():
    return get_all_addresses()


def fetch_address(address_id):
    return get_address(address_id)


def fetch_customer_addresses(customer_id):
    return get_customer_addresses(customer_id)


def add_address(customer_id, address_line, city, state, country, zipcode):
    return create_address(
        customer_id,
        address_line,
        city,
        state,
        country,
        zipcode,
    )


def edit_address(
    address_id,
    address_line,
    city,
    state,
    country,
    zipcode,
):
    return update_address(
        address_id,
        address_line,
        city,
        state,
        country,
        zipcode,
    )


def remove_address(address_id):
    return delete_address(address_id)