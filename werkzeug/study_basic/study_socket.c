#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>  /*Functions: inet_addr*/
#include <string.h>     /*Functions: bzero*/
#include <stdlib.h>     /*Functions: exit*/

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

    sockfd = socket(PF_INET, SOCK_DGRAM, 0);
    if(sockfd < 0) {
        printf("%s\n", "socket error");
        exit(1);
    }

    bzero((char *) &serv, sizeof(serv));
    serv.sin_family = AF_INET;
    /* Convert IP address to 32-bit integer */
    serv.sin_addr.s_addr = inet_addr("10.0.2.15");
    /* small-endian to big-endian*/
    serv.sin_port = htons(8001);

    int send_size = sendto(sockfd, buff, BUFFSIZE, 0, (struct sockaddr *) &serv, sizeof(serv));
    if(send_size != BUFFSIZE) {
        printf("%s\n", "sendto error");
        exit(1);
    }

    n = recvfrom(sockfd, buff, BUFFSIZE, 0, (struct sockaddr *) NULL, (int *) NULL);

    if(n < 2) {
        printf("%s\n", "recvfrom error");
        exit(1);
    }
    printf("%d\n", n);
    printf("%s\n", buff);
    exit(0);
}