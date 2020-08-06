from typing import Dict, List, Optional, Tuple

from boa3.model.builtin.method.builtinmethod import IBuiltinMethod
from boa3.model.expression import IExpression
from boa3.model.type.collection.sequence.sequencetype import SequenceType
from boa3.model.variable import Variable
from boa3.neo.vm.opcode.Opcode import Opcode


class LenMethod(IBuiltinMethod):

    def __init__(self):
        from boa3.model.type.type import Type
        identifier = 'len'
        args: Dict[str, Variable] = {'__o': Variable(Type.sequence)}
        super().__init__(identifier, args, return_type=Type.int)

    def validate_parameters(self, *params: IExpression) -> bool:
        if len(params) != 1:
            return False
        if not isinstance(params[0], IExpression):
            return False
        return isinstance(params[0].type, SequenceType)

    @property
    def opcode(self) -> List[Tuple[Opcode, bytes]]:
        return [(Opcode.SIZE, b'')]

    @property
    def _args_on_stack(self) -> int:
        return len(self.args)

    @property
    def _body(self) -> Optional[str]:
        return None
