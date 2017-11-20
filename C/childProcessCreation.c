#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {

	for(int i = 0; i < 2; i++) {
		printf("\nI'm still alive!");

		int pid = fork();	

		if (pid != 0) {
			// Parent Code
			printf("\nParent Working...\n");
		} else {
			// Child Code
			printf("\nChild Working...\n");			
		}
	}

	return 0;
}
