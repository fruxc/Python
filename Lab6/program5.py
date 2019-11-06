try:
    import sys;
except ImportError:
    print("Could not import sys module \n");
try:
    file=open(input("Enter file name to open\n"),"rt");
    print("File contents \n");
    print(file.read());
except FileNotFoundError:
    print("File was not found, system exiting\n");
    sys.exit(0);
except IOError:
    print("Could not read \n");
    sys.exit(0);
    
try:
    print("Enter two numbers whose division you want to save in a file \n");
    a=int(input());
    b=int(input());
    file.close();
    file=open(input("Enter file name to write \n"),"a");
    file.write(" "+str(a/b));
    file.close();
except FileNotFoundError:
    print("Given file was not found ");
except IOError:
    print("File cannot be opened ");
except ArithmeticError:
    print("Illegal number entered ");
