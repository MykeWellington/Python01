import operacoes 
import pytest

def testar_somar():
    assert operacoes.somar(1,1) == 2
    
def testar_subtrair():
    assert operacoes.subtrair(1,1) == 0
    
def testar_multiplicar():
    assert operacoes.multiplicar(458,7) == 3206
    
def testar_dividir():
    assert operacoes.dividir(4,2) == 2
    with pytest.raises(ValueError):
        operacoes.dividir(1,0)
        
if __name__ == '__main__':
    raise SystemExit(pytest.main([__file__, '-vv']))

        
