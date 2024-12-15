// SPDX-License-Identifier: MIT
pragma solidity 0.8.28;

contract ContractOne {

    mapping (address => uint) public addressBalances;

    function deposit() public payable {
        addressBalances[msg.sender] += msg.value;
    }

    receive() external payable {
        deposit();
    }
}

contract ContractTwo {

    receive() external payable {}

    function depositOnContractOne(address _contractOne) public {
        //ContractOne one = ContractOne(_contractOne);
        //one.deposit{value: 10, gas: 100000}();
        bytes memory payload = abi.encodeWithSignature("deposit()");
        (bool success, ) = _contractOne.call{value: 10, gas: 100000}(payload);
        require(success);
    }
}