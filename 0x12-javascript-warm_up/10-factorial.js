#!/usr/bin/node
function Factorial (num) {
        if (num === 0 || num === 1) {
                return 1;
        }
        else {
                return (num * Factorial (num - 1));
        }
}

if ((process.argv[2]) != undefined && !isNaN(process.argv[2])) {
        console.log(Factorial (Number(process.argv[2])));
} else {
        console.log(1);
}
