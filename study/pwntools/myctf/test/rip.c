#include <stdio.h>

void vuln() {
  int a = 123;
  printf("%p -> %i", &a, a);
}

int main() {
  int b = 321;
  printf("%p -> %i", &b, b);
  vuln();
}
