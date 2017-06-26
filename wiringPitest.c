#include <wiringPi.h>
int main (void)
{
  wiringPiSetup () ;
  pinMode (0, OUTPUT) ;
  for (;;)
  {
    digitalWrite (23, HIGH) ; delay (500) ;
    digitalWrite (23,  LOW) ; delay (500) ;
  }
  return 0 ;
}
