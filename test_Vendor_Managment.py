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
    vm.vendor_id = vm.add_vendors("Vendor 1", "Pizza", "A", vm.vendor_id)
    vm.vendor_id = vm.add_vendors("Vendor 2", "Burger", "B", vm.vendor_id)
    
    assert ValueError 
    
def test_no_value_added():
    vm.vendor_name= ""
    assert ValueError


def test_view_vendor():
    vm.vendor_records.clear()
    vm.vendor_records = {
        "Vendor ID": 0,
        "Vendor Name": "Vendor 1",
        "Food Type": "Pizza",
        "Pitch Location": "A",
    }
    result = vm.view_vendor(0)
    assert result == {
        "Vendor ID": 0,
        "Vendor Name": "Vendor 1",
        "Food Type": "Pizza",
        "Pitch Location": "A",
    }


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
    result = vm.update_vendor(0, "Vendor 1 Updated", "Burgers", "B")
    assert result is True
    assert vm.vendor_records == {
        "Vendor ID": 0,
        "Vendor Name": "Vendor 1 Updated",
        "Food Type": "Burgers",
        "Pitch Location": "B",
    }


def test_delete_vendor():
    vm.vendor_records.clear()
    vm.vendor_records = {
        "Vendor ID": 0,
        "Vendor Name": "Vendor 1",
        "Food Type": "Pizza",
        "Pitch Location": "A",
    }
    result = vm.delete_vendor(0)
    assert result is True
    assert 0 not in vm.vendor_records