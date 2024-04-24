#!/usr/bin/node

const dict = require('./101-data').dict;

function invertDictionary (dictionary) {
  const invertedDict = {};

  for (const userId in dictionary) {
    const occurrences = dictionary[userId];

    if (!invertedDict[occurrences]) {
      invertedDict[occurrences] = [];
    }

    invertedDict[occurrences].push(userId);
  }

  return invertedDict;
}

const invertedDict = invertDictionary(dict);
console.log(invertedDict);
