import pytest
import Vendor_Management as vm

def test_add_vendor():
    vm.vendor_records.clear()
    vm.vendor_id = 0
    vm.vendor_id = vm.add_vendors("Vendor 1", "Pizza", "A", vm.vendor_id)
    vm.vendor_id = vm.add_vendors("Vendor 2", "Burger", "B", vm.vendor_id)
    assert vm.vendor_records == {
        0: {
            "Vendor ID": 0,
            "Vendor Name": "Vendor 1",
            "Food Type": "Pizza",
            "Pitch Location": "A"
        },
        1: {
            "Vendor ID": 1,
            "Vendor Name": "Vendor 2",
            "Food Type": "Burger",
            "Pitch Location": "B"
            
        }
    }

def test_same_vendor_add():
    vm.vendor_records.clear()
    vm.vendor_id = 0

    vm.vendor_id = vm.add_vendors(
        "Vendor 1", "Pizza", "A", vm.vendor_id
    )

    with pytest.raises(ValueError):
        vm.add_vendors("Vendor 2", "Burger", "B", 0)
        
def test_no_value_added():
     with pytest.raises(ValueError):
        vm.add_vendors("", "Pizza", "A", 0)


def test_delete_vendor():
    vm.vendor_records.clear()

    vm.vendor_records[0] = {
        "Vendor ID": 0,
        "Vendor Name": "Vendor 1",
        "Food Type": "Pizza",
        "Pitch Location": "A"
    }

    vm.delete_vendors(0)

    assert 0 not in vm.vendor_records
    
def test_vendor_delete_out_of_range():
    vm.vendor_records.clear()

    vm.vendor_records[0] = {
        "Vendor ID": 0,
        "Vendor Name": "Vendor 1",
        "Food Type": "Pizza",
        "Pitch Location": "A"
    }

    with pytest.raises(KeyError):
        vm.delete_vendors(1)
        
def test_vendor_delete_empty():
    with pytest.raises(ValueError):
        vm.delete_vendors("")

def test_view_vendor():
    vm.vendor_records.clear()

    vm.vendor_records[0] = {
        "Vendor ID": 0,
        "Vendor Name": "Vendor 1",
        "Food Type": "Pizza",
        "Pitch Location": "A"
    }

    assert vm.view_vendor(0) == (
        "Vendor ID: 0\n"
        "Vendor Name: Vendor 1\n"
        "Food Type: Pizza\n"
        "Pitch Location: A\n"
    )    
def test_view_out_of_range():
    vm.vendor_records.clear()

    with pytest.raises(KeyError):
        vm.view_vendor(1)
def test_nothing_entered_in_view():
    with pytest.raises(ValueError):
        vm.view_vendor("")

def test_view_all_vendor():
    vm.vendor_records.clear()
    vm.vendor_records = {
        "Vendor ID": 0,
        "Vendor Name": "Vendor 1",
        "Food Type": "Pizza",
        "Pitch Location": "A",
    }
    result = vm.view_all_vendor()
    assert result == {
        0: {
            "Vendor ID": 0,
            "Vendor Name": "Vendor 1",
            "Food Type": "Pizza",
            "Pitch Location": "A",
        }
    }

def test_update_vendor():
    vm.vendor_records.clear()
    vm.vendor_records = {
        "Vendor ID": 0,
        "Vendor Name": "Vendor 1",
        "Food Type": "Pizza",
        "Pitch Location": "A",
    }
    vm.update_vendor(0, "Vendor 1 Updated", "Burgers", "B")
    assert vm.vendor_records == {
        "Vendor ID": 0,
        "Vendor Name": "Vendor 1 Updated",
        "Food Type": "Burgers",
        "Pitch Location": "B",
    }
    
def test_vendor_updated_out_of_range():
    vm.vendor_records.clear()
    
    with pytest.raises(KeyError):
        vm.update_vendor(1)