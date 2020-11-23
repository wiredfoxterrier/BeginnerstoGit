//Ansh Sharma 
import java.util.*;
public class practice1
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner (System.in);
		int arr[][] = new int[3][3];
		int i,j;
		for( i = 0;i<3;i++)
		{
			for(j = 0 ; j<3;j++)
			{
				System.out.println("Enter Element");
				arr[i][j]=sc.nextInt();
			}
		}
		System.out.println("Input");
		for( i = 0;i<3;i++)
		{
			for( j = 0 ; j<3;j++)
			{
				System.out.print(arr[i][j]+" ");

			}
			System.out.println("");
		}
		int temp;
		int C = 100;
		for(i = 0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
				temp = arr[i][j]+ C;
				arr[i][j]=arr[j][i];
				arr[j][i]= temp -C;

			}
		}
		System.out.println("Output");

		for( i = 0;i<3;i++)
		{
			for( j = 0 ; j<3;j++)
			{
				System.out.print(arr[i][j]+" ");

			}
			System.out.println("");
		}
	}
}