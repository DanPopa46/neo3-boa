from typing import Dict

from boa3.model.builtin.interop.contract.contractmanagementmethod import ContractManagementMethod
from boa3.model.variable import Variable


class DestroyMethod(ContractManagementMethod):

    def __init__(self):
        from boa3.model.type.type import Type
        identifier = 'destroy_contract'
        syscall = 'destroy'
        args: Dict[str, Variable] = {}
        super().__init__(identifier, syscall, args, return_type=Type.none)
