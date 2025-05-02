#include <stdio.h>

void win() {
  char flag[30];
  FILE *fd = fopen("flag.txt", "r");
  fgets(flag, sizeof(flag), fd);
  printf("%s", flag);
}

void vuln() {
  char fmt_str[50];
  printf("Entered next phase\n");

  /*void *local_var_addr = __builtin_frame_address(0); // This gives current RBP
  void **ret_addr = (void **)((char *)local_var_addr + 8); // RIP is at RBP+8

  printf("rip -> %p\n", ret_addr);
  printf("rbp -> %p\n", local_var_addr);*/

  scanf("%s", fmt_str);
  printf(fmt_str);
}

int main() {
  int b = 222;
  char buff_overflow1[30];

  printf("buff1 is at %p\n", buff_overflow1);
  printf("b: %p -> %i\n", &b, b);

  printf("Input buffer overflow, to make b == 12312369: ");
  scanf("%s", buff_overflow1);

  printf("b: %p -> %i\n", &b, b);

  if (b == 12312369)
    vuln();
  return 0;
}
