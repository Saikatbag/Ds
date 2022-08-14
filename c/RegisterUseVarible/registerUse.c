#include <stdio.h>
#include <time.h>   	// for clock_t, clock(), CLOCKS_PER_SEC
#include <unistd.h> 	// for sleep()

int main()
{
	double time_spent = 0.0;

	clock_t begin = clock();
	register long int i =0;
	for(i;i<9999999999;i++){
		
	}
	clock_t end = clock();
	time_spent = (end - begin)/60 ;


	double time_spent2 = 0.0;

        clock_t begin2 = clock();
        long int i2 =0;
        for(i2;i2<9999999999;i2++){
                
        }
        clock_t end2 = clock();
        time_spent2 = (end2 - begin2)/60 ;

        printf("The elapsed time is %f min", time_spent2);
	 printf("The elapsed time is register %f min", time_spent);

	return 0;
}
