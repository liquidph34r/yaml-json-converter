"use strict";
exports.__esModule = true;
//Should be input line by line
var fs = require("fs");
var readfile = fs.readFileSync('./convert/sample2.yaml', 'utf-8');
var splitfile = readfile.split('\n');
var stack;
stack = ['  '];
var symstack;
console.log("{");
symstack = ["{"];
var index = 0;
splitfile.forEach(function (line) {
    index++;
    line = line.substring(0, line.length - 1);
    if (line.trim().startsWith('-') && line.includes(':')) {
        console.log(stack.toString() + '{');
        if (Number(line.substring(line.lastIndexOf(": ") + 2))) {
            console.log(stack.toString() + '  "' + line.trimStart().substring(2, line.indexOf(":") - 2) + '": ' + Number(line.substring(line.lastIndexOf(": ") + 2)));
        }
        else if (line.substring(line.lastIndexOf(":")).length == 1) {
            console.log(stack.toString() + '  "' + line.trimStart().substring(2, line.indexOf(":") - 2) + '": ' + 'null');
        }
        else if (line.substring(line.lastIndexOf(": ") + 2) == "true") {
            console.log(stack.toString() + '  "' + line.trimStart().substring(2, line.indexOf(":") - 2) + '": ' + 'true');
        }
        else if (line.substring(line.lastIndexOf(": ") + 2) == "false") {
            console.log(stack.toString() + '  "' + line.trimStart().substring(2, line.indexOf(":") - 2) + '": ' + 'false');
        }
        else {
            console.log(stack.toString() + '  "' + line.trimStart().substring(2, line.indexOf(":") - 2) + '": "' + line.substring(line.lastIndexOf(": ") + 2) + '"');
        }
        console.log(stack.toString() + '},');
        return;
    }
    else if (line.startsWith('-')) {
        console.log(stack.toString() + '"' + line.substring(2) + '",');
        return;
    }
    if (line.endsWith(':')) {
        if (symstack[symstack.length - 1] == '[') {
            stack.pop();
            console.log(stack.toString() + "],");
            symstack.pop();
        }
        if (splitfile[index].trim().startsWith('-')) {
            console.log(stack.toString() + '"' + line.slice(0, line.length - 1).trim() + '": [');
            symstack.push("[");
            //console.log(symstack);
            stack.push('  ');
        }
        else {
            console.log(stack.toString() + '"' + line.slice(0, line.length - 1).trim() + '": {');
            symstack.push("{");
            //console.log(symstack);
            stack.push('  ');
        }
        return;
    }
    /*
    if(line.substring(0, line.length-1)== "|" ||line.substring(0, line.length-2)== "|-"){
        //need to make sure this appends - unfinsihed
        console.log(stack.toString()+ '  "' + line.trimStart().substring(2, line.indexOf(":"))+'": "')
        return
    }
    console.log(line.trim()+"\\" + "n"); // this needs to append
    if (splitfile[index].trim().startsWith("-") || splitfile[index].endsWith(":")){
        //console.log(line.trim()+"\\" + 'n",');
    }
    */
});
