#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  if (theFunction) {
    return number + 1;
  }
};
