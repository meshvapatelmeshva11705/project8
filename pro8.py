import numpy as np


class DataAnalytics:

    def __init__(self):
        self.array = None

    @classmethod
    def project_info(cls):
        print("="*45)
        print("      NUMPY DATA ANALYZER")
        print("="*45)
    @staticmethod
    def line():
        print("-" * 45)

    def create_array(self):
        DataAnalytics.line() 
        print("\n-- ARRAY CREATION --")
        DataAnalytics.line() 
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:

            n = int(input("\nEnter the number of elements: "))

            print("Enter", n, "elements separated by space:")
            arr = list(map(int, input().split()))

            self.array = np.array(arr)

        elif choice == 2:

            r = int(input("\nEnter number of rows: "))
            c = int(input("Enter number of columns: "))

            print("Enter", r * c, "elements separated by space:")
            arr = list(map(int, input().split()))

            self.array = np.array(arr).reshape(r, c)

        elif choice == 3:

            d = int(input("\nEnter number of matrices (depth): "))
            r = int(input("Enter number of rows: "))
            c = int(input("Enter number of columns: "))

            print("Enter", d * r * c, "elements separated by space:")
            arr = list(map(int, input().split()))

            self.array = np.array(arr).reshape(d, r, c)

        else:
            print("\nInvalid Choice!")
            return

        print("\nArray Created Successfully!")
        print("\nOriginal Array:")
        print(self.array)

        if self.array.ndim == 2:
            self.indexing_slicing()

    def indexing_slicing(self):

        while True:
            DataAnalytics.line() 
            print("-- INDEXING & SLICING --")
            DataAnalytics.line() 
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:

                print("\nOriginal Array:")
                print(self.array)

                r = int(input("\nEnter Row Index: "))
                c = int(input("Enter Column Index: "))

                print("\nSelected Element:")
                print(self.array[r][c])

            elif choice == 2:

                print("\nOriginal Array:")
                print(self.array)

                rs = input("\nEnter Row Range (start:end): ")
                cs = input("Enter Column Range (start:end): ")

                r1, r2 = map(int, rs.split(":"))
                c1, c2 = map(int, cs.split(":"))

                print("\nSliced Array:")
                print(self.array[r1:r2, c1:c2])

            elif choice == 3:
                break

            else:
                print("\nInvalid Choice!")

    def menu(self):

        while True:
            DataAnalytics.project_info()
            DataAnalytics.line()

            print("--- WELCOME TO NUMPY ANALYZER ---")
            
            print("1. Array Creation")
            print("2. Mathematical Operations")
            print("3. Combine / Split Arrays")
            print("4. Search / Sort / Filter")
            print("5. Aggregate & Statistics")
            print("6. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.create_array()

            elif choice == 2:
                self.mathematical_operations()

            elif choice == 3:
                self.combine_split()

            elif choice == 4:
                self.search_sort_filter()

            elif choice == 5:
                self.aggregate_statistics()

            elif choice == 6:
                print("\nThank You For Using NumPy Analyzer!")
                print("Goodbye...")
                break

            else:
                print("\nInvalid Choice!")

    def mathematical_operations(self):

        if self.array is None:
            print("\nPlease create an array first.")
            return
        DataAnalytics.line() 
        print("-- MATHEMATICAL OPERATIONS --")
        DataAnalytics.line() 
        print("\nOriginal Array:")
        print(self.array)

        print("\nChoose an Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("\nEnter your choice: "))

        if choice in [1, 2, 3, 4]:

            print("\nEnter", self.array.size,
                "elements for second array:")

            arr = list(map(int, input().split()))
            arr2 = np.array(arr).reshape(self.array.shape)

            print("\nSecond Array:")
            print(arr2)

            if choice == 1:
                print("\nResult of Addition:")
                print(self.array + arr2)

            elif choice == 2:
                print("\nResult of Subtraction:")
                print(self.array - arr2)

            elif choice == 3:
                print("\nResult of Multiplication:")
                print(self.array * arr2)

            elif choice == 4:
                print("\nResult of Division:")
                print(self.array / arr2)

        else:
            print("\nInvalid Choice!")

    def combine_split(self):

        if self.array is None:
            print("\nPlease create an array first.")
            return
    
        DataAnalytics.line()
        print("-- COMBINE / SPLIT ARRAYS --")
        DataAnalytics.line() 
        print("\nOriginal Array:")
        print(self.array)

        print("\nChoose an Operation:")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:

            print("\nEnter", self.array.size,
                "elements for second array:")

            arr = list(map(int, input().split()))
            arr2 = np.array(arr).reshape(self.array.shape)

            print("\nSecond Array:")
            print(arr2)

            result = np.vstack((self.array, arr2))

            print("\nCombined Array:")
            print(result)

        elif choice == 2:

            parts = int(input("\nEnter number of parts: "))

            result = np.array_split(self.array, parts)

            print("\nSplit Arrays:")

            for i in range(len(result)):
                print(f"\nPart {i+1}:")
                print(result[i])

        else:
            print("\nInvalid Choice!")

    def search_sort_filter(self):

        if self.array is None:
            print("\nPlease create an array first.")
            return

        DataAnalytics.line()
        print("\n-- SEARCH / SORT / FILTER --")
        DataAnalytics.line()

        print("\nOriginal Array:")
        print(self.array)

        print("\nChoose an Operation:")
        print("1. Search Element")
        print("2. Sort Array")
        print("3. Filter Even Numbers")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:

            key = int(input("\nEnter element to search: "))

            pos = np.where(self.array == key)

            if len(pos[0]) == 0:
                print("\nElement not found.")

            else:
                print("\nElement found at index:")
                print(pos)

        elif choice == 2:

            print("\nSorted Array:")
            print(np.sort(self.array))

        elif choice == 3:

            print("\nFiltered Even Numbers:")
            print(self.array[self.array % 2 == 0])

        else:
            print("\nInvalid Choice!")

    def aggregate_statistics(self):

        if self.array is None:
            print("\nPlease create an array first.")
            return

        DataAnalytics.line()
        print("-- AGGREGATE & STATISTICS --")
        DataAnalytics.line()

        print("\nOriginal Array:")
        print(self.array)

        print("\nChoose an Operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
    
        choice = int(input("\nEnter your choice: "))

        if choice == 1:

            print("\nSum of Array:")
            print(np.sum(self.array))

        elif choice == 2:

            print("\nMean of Array:")
            print(np.mean(self.array))

        elif choice == 3:

            print("\nMedian of Array:")
            print(np.median(self.array))

        elif choice == 4:

            print("\nStandard Deviation:")
            print(np.std(self.array))

        elif choice == 5:

            print("\nVariance:")
            print(np.var(self.array))

        
        else:
            print("\nInvalid Choice!")

obj = DataAnalytics()
obj.menu()

