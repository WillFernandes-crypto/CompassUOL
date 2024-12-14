// SPDX-License-Identifier: MIT
pragma solidity 0.8.28;

contract ExampleWrapAround {

    uint256 public myUint; // 0 - 2^(256)-1

    uint8 public myUint8 = 250;

    int public myInt = -10; // -2^128 para +2^128

    function setMyUint(uint _myuint) public {
        myUint = _myuint;
    }

    function decreementUInt() public {
        myUint--;
    }

    function increementeUint8() public {
        myUint8++;
    }

    function increementInt() public {
        myInt++;
    }
}