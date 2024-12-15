// SPDX-License-Identifier: MIT
pragma solidity 0.8.28;

contract SampleContract {

    string public myString = "Hello World";

    function updateString(string memory _newString) public {
        myString = _newString;
    }

    function payableUpdateString(string memory _newPayableString) public payable {
        if (msg.value == 1 ether) {
            myString = _newPayableString;
        } else {
            payable(msg.sender).transfer(msg.value);
        }
    }
}