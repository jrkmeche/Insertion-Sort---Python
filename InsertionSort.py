class InsertionSort:
    def __init__(self, integerList):
        self.integerList = integerList

    def sort(self):
        print("sort called")
        #for loop for iterating through a integerList of "n" numbers
        #starting at index 1 and ending at the length of the
        #array. If the nth number is less than the (n-1)th
        #number, the elements is swapped. This will sort the 
        #integerList into ascending order
        #Time complexity Avg: O(n)
        #Time Complexity WCS: O(n^2)
        for i in range(1, len(self.integerList)):
            unsortedIntValue = self.integerList[i]

            j = i - 1
            while (j >= 0 and unsortedIntValue < self.integerList[j]):
                self.integerList[j + 1] = self.integerList[j]
                j -= 1
            self.integerList[j + 1] = unsortedIntValue

    def print_sorted_list(self):
        print("Sorted integerList: ", self.integerList)
        
if __name__ == "__main__":
    integerList = [12, 11, 13, 5, 6, 100, 87, 345, 9238, 2]
    print(integerList)
    sorter = InsertionSort(integerList)
    sorted_integerList = sorter.sort()
    sorter.print_sorted_list()





