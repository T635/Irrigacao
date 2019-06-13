#include <VirtualWire.h>
#include <stdio.h>
#include <string.h>
char a;
int b;
void setup()
{
    Serial.begin(9600); 
    vw_set_ptt_inverted(true);
    vw_setup(2000); 
    pinMode(6, OUTPUT);
    digitalWrite(6, HIGH);
    vw_rx_start();  
}

void loop()
{
    uint8_t buf[VW_MAX_MESSAGE_LEN];
    uint8_t buflen = VW_MAX_MESSAGE_LEN;
    if (vw_get_message(buf, &buflen))
    {
  int i;
  for (i = 0;i < buflen; i++)
  {
      
      a = char(buf[i]);
      b = int(a);
      Serial.println(b);
      if (b == 48)
      { digitalWrite(6,LOW);
         
      }
      else if (b == 49)
      { digitalWrite(6, HIGH);
      }
      
  } 
    }
}
