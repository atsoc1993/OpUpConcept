from algopy import ARC4Contract, OpUpFeeSource, ensure_budget, UInt64, urange, log, Global, op
from algopy.arc4 import abimethod
from algopy.arc4 import UInt64 as arc4UInt64



class TestOpcodeBudget(ARC4Contract):
    def __init__(self) -> None:
        pass
    
    @abimethod(allow_actions=['UpdateApplication', 'DeleteApplication'])
    def update_or_delete_placeholder(
        self
    ) -> None:
        pass



  

    @abimethod
    def op_up_simple_example(
        self,
        y: UInt64
    ) -> tuple[UInt64, UInt64]:
        opups_used = UInt64(0)
        x = UInt64(0)
        for i in urange(y):
            x += 1
            if Global.opcode_budget() < 100:
                opups_used += 1
                ensure_budget(700, fee_source= OpUpFeeSource.GroupCredit)
            log(arc4UInt64(Global.opcode_budget()).bytes)


        return x, opups_used



  
    
    @abimethod
    def arbitrary_opcode_monitoring(
        self,
        iterations: UInt64
    ) -> None:
        
        hash = op.sha256(
            arc4UInt64(Global.round).bytes
        )
        
        #waste opcodes for checking budget changes
        for i in urange(iterations):
            waste_opcodes_1 = op.sha256(hash)
            waste_opcodes_2 = UInt64(1) + UInt64(1)
            waste_opcodes_3 = arc4UInt64.from_bytes(
                arc4UInt64(0).bytes
            )
            for j in urange(10):
                waste_opcodes_4 = i + j
                waste_opcodes_5 = i + UInt64(1)
                waste_opcodes_6, waste_opcodes_7 = op.mulw((UInt64(2**32) - 1), 10)
                
            #log how many opcodes are remaining
            log(
                arc4UInt64(Global.opcode_budget())
            )
            
            
            
