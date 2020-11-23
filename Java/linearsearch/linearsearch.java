//Ansh Sharma
//2nd October 2020
import java.util.*;
public class linearsearch
{
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter Number of elements"); //Enter number of elements in the array
		int n= sc.nextInt();//Stores user input for number of elements
		int a [] = new int[n];//Creating the array
		for(int i = 0;i<n;i++)//Filling of array
		{
			System.out.println("Enter element");
			a[i] = sc.nextInt();//Stores the value of element entered

		}
		System.out.println("Enter the item to be found");
		int item = sc.nextInt();
		linearsearch object = new linearsearch();//Creation of object of class
		int loc = object.search(a,n,item);//Caling of object and storing returned value in variable loc
		if(loc>=0)
		{
			System.out.println("The first number is at position number  "+ (loc+1)); 
		}
		else
		{
			System.out.println("The number is not in the array entered");
		}
	}
	public int search(int a[], int n, int item)
	{
		for(int i = 0;i<n;i++)//Searching of array
		{
			if(a[i]==item)//Checking if item is in array or not.
			{
				return i;
			}

		}
		return -1;
	}
}