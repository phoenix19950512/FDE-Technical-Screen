from sort_packages import sort

def test_sort_packages():
    # Test standard packages
    assert sort(100, 100, 50, 10) == "STANDARD"
    
    # Test bulky packages (by volume)
    assert sort(100, 100, 100, 10) == "SPECIAL"
    
    # Test bulky packages (by dimension)
    assert sort(160, 50, 50, 10) == "SPECIAL"
    
    # Test heavy packages
    assert sort(50, 50, 50, 25) == "SPECIAL"
    
    # Test rejected packages (both bulky and heavy)
    assert sort(150, 150, 150, 25) == "REJECTED"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_sort_packages()
