#include <stdio.h>
//#include <sys/socket.h>
#include <netinet/in.h>

#define BUFFSIZE 150 /* arbitary size*/

/*
struct sockaddr {
    u_char sa_len;          // total leagth
    u_char sa_family;       // address family
    u_char sa_data[14];     // actually longer; address value
};
*/
/*sa_family: AF_INET, AF_ISO, AF_OSI, AF_UNIX, AF_ROUTE, AF_LINK, AF*/

/*
struct in_addr {
    u_long s_addr;          // 32-bit IP address, net byte order
}

struct sockaddr_in {
    u_char sin_len;             // sizeof(struct sockaddr_in) = 16
    u_char sin_family;          // AF_INET (is a int number, value is 2)
    u_short sin_port;           // 16-bit port number, net byte order
    struct in_addr sin_addr;    //
    char sin_zero[8];           // unused
}
*/

int main() {
    struct sockaddr_in serv;
    char buff[BUFFSIZE];
    int sockfd, n;

    printf("%d\n", AF_INET);
}