#Lab 2 (part2)
#student name:Nikoo Vali
#student number:83343012

from tkinter import *
# do not import any more modules

# do not change the skeleton of the program. Only add code where it is requested.
class ComplexNumber:
    """ this class implements the complex number type
        it stores the complex number in Cartesian form
        two data fields:
            real and imaginary
        Operations:
            add, subtract, multiply, divide
            toString
    """
    def __init__(self, real: float, imaginary: float) -> None:
        """Initializer stores the real and imaginary parts"""
        self.real = real
        self.imaginary = imaginary

    def add(self, secondComplex):
        """Adds 'this' complex number to secondComplex
        Returns the result as a ComplexNumber
        """
        real_part = self.real + secondComplex.real
        imaginary_part = self.imaginary + secondComplex.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def subtract(self, secondComplex):
        """Subtracts secondComplex from 'this' complex number
        Returns the result as a ComplexNumber
        """
        real_part = self.real - secondComplex.real
        imaginary_part = self.imaginary - secondComplex.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def multiply(self, secondComplex):
        """Multiplies 'this' complex number with secondComplex
        Returns the result as a ComplexNumber
        """
        real_part = (self.real * secondComplex.real) - (self.imaginary * secondComplex.imaginary)
        imaginary_part = (self.real * secondComplex.imaginary) + (self.imaginary * secondComplex.real)
        return ComplexNumber(real_part, imaginary_part)

    def divide(self, other):
        # Check if the denominator (other) is zero
        if other.real == 0 and other.imaginary == 0:
            # Return NaN if dividing by zero
            return ComplexNumber(float('nan'), float('nan'))
    
        # Perform standard division of complex numbers if denominator is not zero
        denominator = (other.real ** 2 + other.imaginary ** 2)
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
    
        # Return the result as a new ComplexNumber instance
        return ComplexNumber(real_part, imaginary_part)

    def toString(self):
        """Returns a string representation of 'this' complex number
        Formats:
        - "a + bi"
        - "a - bi"
        - "a" (if imaginary part is 0)
        - "bi" (if real part is 0)
        - "NaN" (if any part is NaN)
        - "i" or "-i" (if imaginary part is 1 or -1 respectively)
        """
        if any([str(self.real) == 'nan', str(self.imaginary) == 'nan']):
            return "NaN"
        real_zero = self.real == 0
        imaginary_zero = self.imaginary == 0

        if real_zero and imaginary_zero:
            return "0"
        elif imaginary_zero:
            return str(self.real)
        elif real_zero:
            if self.imaginary == 1:
                return "i"
            elif self.imaginary == -1:
                return "-i"
            else:
                return f"{self.imaginary}i"
        else:
            # Handle the sign for the imaginary part
            if self.imaginary > 0:
                if self.imaginary == 1:
                    return f"{self.real} + i"
                else:
                    return f"{self.real} + {self.imaginary}i"
            else:
                if self.imaginary == -1:
                    return f"{self.real} - i"
                else:
                    return f"{self.real} - {-self.imaginary}i"

class GUI:
    """ this class implements the GUI for our program
        use as is.
        The add, subtract, multiply and divide methods invoke the corresponding
        methods from the ComplexNumber class to calculate the result to display.
    """
    def __init__(self):
        """ The initializer creates the main window, label and entry widgets,
            and starts the GUI mainloop.
        """
        window = Tk()
        window.title("Complex Numbers")

        # Labels and entries for the first complex number
        frame1 = Frame(window)
        frame1.grid(row = 1, column = 1, pady = 10)
        Label(frame1, text = "Complex 1:").pack(side = LEFT)
        self.complex1Real = StringVar()
        Entry(frame1, width = 5, textvariable = self.complex1Real, 
            justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame1, text = "+").pack(side = LEFT)
        self.complex1Imaginary = StringVar()
        Entry(frame1, width = 5, textvariable = self.complex1Imaginary, 
            justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame1, text = "i").pack(side = LEFT)

        # Labels and entries for the second complex number
        frame2 = Frame(window)
        frame2.grid(row = 3, column = 1, pady = 10)
        Label(frame2, text = "Complex 2:").pack(side = LEFT)
        self.complex2Real = StringVar()
        Entry(frame2, width = 5, textvariable = self.complex2Real, 
            justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame2, text = "+").pack(side = LEFT)
        self.complex2Imaginary = StringVar()
        Entry(frame2, width = 5, textvariable = self.complex2Imaginary, 
            justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame2, text = "i").pack(side = LEFT)

        # Labels and entries for the result complex number
        # An entry widget is used as the output here
        frame3 = Frame(window)
        frame3.grid(row = 4, column = 1, pady = 10)
        Label(frame3, text = "Result:     ").pack(side = LEFT)
        self.result = StringVar()
        Entry(frame3, width = 20, textvariable = self.result, 
            justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)

        # Buttons for add, subtract, multiply and divide
        frame4 = Frame(window)  # Create and add a frame to window
        frame4.grid(row = 5, column = 1, pady = 5, sticky = E)
        Button(frame4, text = "Add", command = self.add).pack(side = LEFT)
        Button(frame4, text = "Subtract", command = self.subtract).pack(side = LEFT)
        Button(frame4, text = "Multiply", command = self.multiply).pack(side = LEFT)
        Button(frame4, text = "Divide", command = self.divide).pack(side = LEFT)

        mainloop()

    def add(self): 
        (complex1, complex2) = self.getBothComplex()
        result = complex1.add(complex2)
        self.result.set(result.toString())

    def subtract(self):
        (complex1, complex2) = self.getBothComplex()
        result = complex1.subtract(complex2)
        self.result.set(result.toString())

    def multiply(self):
        (complex1, complex2) = self.getBothComplex()
        result = complex1.multiply(complex2)
        self.result.set(result.toString())

    def divide(self):
        (complex1, complex2) = self.getBothComplex()
        result = complex1.divide(complex2)
        self.result.set(result.toString())

    def getBothComplex(self):
        """ Helper method used by add, subtract, multiply and divide methods """
        try:
            real1 = float(self.complex1Real.get())
            imaginary1 = float(self.complex1Imaginary.get())
            complex1 = ComplexNumber(real1, imaginary1)

            real2 = float(self.complex2Real.get())
            imaginary2 = float(self.complex2Imaginary.get())
            complex2 = ComplexNumber(real2, imaginary2)
            return (complex1, complex2)
        except:
            return (ComplexNumber(float('nan'), float('nan')), ComplexNumber(float('nan'), float('nan')))  # NaN

if __name__ == "__main__":
    GUI()
