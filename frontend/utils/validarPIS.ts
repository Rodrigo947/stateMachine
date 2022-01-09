
 
export default function validarPIS(pis: string): boolean {
  const numPIS = pis.replace(/\./g, '').replace(/-/g, '')
  
  const pesos = "3298765432"
  let total = 0
  let resto
  let resultado
 			
	if (numPIS === "" || numPIS == null)	{
		return false
	}
	
	for(let i = 0; i <= 9; i++) {
		resultado = parseInt(numPIS.slice(i,i+1)) * parseInt(pesos.slice(i,i+1));
		total = total + resultado
	}
	
	resto = (total % 11)
	
	if (resto !== 0) resto = 11 - resto
	
	if (resto === 10 || resto === 11) resto = 0
	
	if (resto !== parseInt(numPIS.slice(10,11))) return false
	
	return true
}
 