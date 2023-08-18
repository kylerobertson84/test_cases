class TestCase:

    def __init__(self, test_case, A, B):
        self.test_case = test_case
        self.A = A
        self.B = B

    # Subtract
    
    def Program_given(self):
        temp_A = self.A - self.B
        C = temp_A * 2
        return C
    
    def Subtract_Sum(self):
        temp_A = self.A - self.B
        C = temp_A + 2
        return C
    
    def Subtract_Divide(self):
        temp_A = self.A - self.B
        C = temp_A / 2
        return C
    
    def Subtract_Subtract(self):
        temp_A = self.A - self.B
        C = temp_A - 2
        return C
    
    # Sum
    
    def Sum_Prod(self):
        temp_A = self.A + self.B
        C = temp_A * 2
        return C
    
    def Sum_Sum(self):
        temp_A = self.A + self.B
        C = temp_A + 2
        return C
    
    def Sum_Divide(self):
        temp_A = self.A + self.B
        C = temp_A / 2
        return C
    
    def Sum_Subtract(self):
        temp_A = self.A + self.B
        C = temp_A - 2
        return C
    
    # Divide

    def Divide_Prod(self):
        temp_A = self.A / self.B
        C = temp_A * 2
        return C
    
    def Divide_Sum(self):
        temp_A = self.A / self.B
        C = temp_A + 2
        return C
    
    def Divide_Divide(self):
        temp_A = self.A / self.B
        C = temp_A / 2
        return C
    
    def Divide_Subtract(self):
        temp_A = self.A / self.B
        C = temp_A - 2
        return C

    # Product 

    def Prod_Prod(self):
        temp_A = self.A * self.B
        C = temp_A * 2
        return C
    
    def Prod_Sum(self):
        temp_A = self.A * self.B
        C = temp_A + 2
        return C
    
    def Prod_Divide(self):
        temp_A = self.A * self.B
        C = temp_A / 2
        return C
    
    def Prod_Subtract(self):
        temp_A = self.A * self.B
        C = temp_A - 2
        return C
    
    def All_Methods(self):
        #Subtract
        print("program = ",self.Program_given())
        print("- + = ",self.Subtract_Sum())
        print("- / = ",self.Subtract_Divide())
        print("- - = ",self.Subtract_Subtract())
        #Sum
        print("+ / = ",self.Sum_Divide())
        print("+ * = ",self.Sum_Prod())
        print("+ - = ",self.Sum_Subtract())
        print("+ + = ",self.Sum_Sum())

        #Divide
        print("/ / = ",self.Divide_Divide())
        print("/ * = ",self.Divide_Prod())
        print("/ - = ",self.Divide_Subtract())
        print("/ + = ",self.Divide_Sum())

        #Product
        print("* / = ",self.Prod_Divide())
        print("* * = ",self.Prod_Prod())
        print("* - = ",self.Prod_Subtract())
        print("* + = ",self.Prod_Sum())
    
    def get_a(self):
        return self.A
    
    def get_b(self):
        return self.B
    
    def set_A(self, A):
        self.A = A
    
    def set_B(self, B):
        self.B = B

    def test_details(self):
        print(self.test_case, ": ","A = ", self.get_a(), " B = ", self.get_b())

    def FindFailedTests(self):
        if(self.Program_given() == self.Subtract_Sum()):

            return True
        elif(self.Program_given() == self.Subtract_Divide()):

            return True
        elif(self.Program_given() == self.Subtract_Subtract()):

            return True
        elif(self.Program_given() == self.Sum_Divide()):

            return True
        elif(self.Program_given() == self.Sum_Prod()):

            return True
        elif(self.Program_given() == self.Sum_Subtract()):

            return True
        elif(self.Program_given() == self.Sum_Sum()):

            return True
        elif(self.Program_given() == self.Divide_Divide()):

            return True
        elif(self.Program_given() == self.Divide_Prod()):

            return True
        elif(self.Program_given() == self.Divide_Subtract()):
    
            return True
        elif(self.Program_given() == self.Divide_Sum()):
    
            return True
        elif(self.Program_given() == self.Prod_Divide()):
    
            return True
        elif(self.Program_given() == self.Prod_Prod()):
    
            return True
        elif(self.Program_given() == self.Prod_Subtract()):
    
            return True
        elif(self.Program_given() == self.Prod_Sum()):
    
            return True
        else:
            return False