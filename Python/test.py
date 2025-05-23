def faculteit(n):
    totaal = 1
    while n > 1:
        totaal *= n
        return n
if __name__ == "__main__":
    print("--start test--")
    
    print(faculteit(0))
    print(faculteit(1))
    print(faculteit(2))
    print(faculteit(3))
    print(faculteit(4))
    print(faculteit(5))
    
    print("--einde test--")
