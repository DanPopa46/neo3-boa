from typing import Dict

from boa3.model.builtin.interop.contract.contractmanagementmethod import ContractManagementMethod
from boa3.model.builtin.interop.contract.contracttype import ContractType
from boa3.model.variable import Variable


class GetContractMethod(ContractManagementMethod):

    def __init__(self, contract_type: ContractType):
        from boa3.model.type.collection.sequence.uint160type import UInt160Type
        identifier = 'get_contract'
        syscall = 'getContract'
        args: Dict[str, Variable] = {'hash': Variable(UInt160Type.build())}
        super().__init__(identifier, syscall, args, return_type=contract_type)
