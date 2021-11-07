#ifndef GETOPT_H
#define GETOPT_H

extern char *optarg;
extern int   optind;

//function in the header file that allows to 
//receive data from user if is necesary instead of 
//automatic data in the new implementation made by me.
int getopt (int nargc, char * const nargv[], const char *ostr);

#endif

