"""
Módulo para calcular números 'bouncy' (números que no son ni crecientes ni decrecientes).

Un número es 'bouncy' si no cumple con ninguna de estas condiciones:
- Creciente: ningún dígito es mayor que el dígito a su izquierda (ej: 134468)
- Decreciente: ningún dígito es mayor que el dígito a su derecha (ej: 66420)
"""

from typing import Tuple


class BouncyNumberCalculator:
    """Clase para calcular y analizar números bouncy."""
    
    @staticmethod
    def is_bouncy(number: int) -> bool:
        """
        Determina si un número es bouncy.
        
        Args:
            number: El número a evaluar
            
        Returns:
            bool: True si el número es bouncy, False en caso contrario
        """
        if number < 100:  # Los números menores a 100 no pueden ser bouncy
            return False
            
        digits = str(number)
        return not (BouncyNumberCalculator._is_increasing(digits) or 
                   BouncyNumberCalculator._is_decreasing(digits))
    
    @staticmethod
    def _is_increasing(digits: str) -> bool:
        """Verifica si los dígitos están en orden creciente o igual."""
        return all(int(digits[i]) <= int(digits[i+1]) 
                  for i in range(len(digits)-1))
    
    @staticmethod
    def _is_decreasing(digits: str) -> bool:
        """Verifica si los dígitos están en orden decreciente o igual."""
        return all(int(digits[i]) >= int(digits[i+1]) 
                  for i in range(len(digits)-1))
    
    @staticmethod
    def find_proportion_threshold(target_percentage: float) -> Tuple[int, float]:
        """
        Encuentra el primer número donde la proporción de números bouncy 
        alcanza o supera el porcentaje objetivo.
        
        Args:
            target_percentage: Porcentaje objetivo (0-100)
            
        Returns:
            Tuple[int, float]: (número encontrado, porcentaje exacto)
        """
        if not 0 <= target_percentage <= 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
            
        bouncy_count = 0
        current_number = 0
        target_ratio = target_percentage / 100
        
        while True:
            current_number += 1
            if BouncyNumberCalculator.is_bouncy(current_number):
                bouncy_count += 1
            
            current_ratio = bouncy_count / current_number
            if current_ratio >= target_ratio:
                return current_number, current_ratio * 100


def main():
    """Función principal que ejecuta el cálculo para el 99%."""
    try:
        calculator = BouncyNumberCalculator()
        target_percentage = 99
        result, exact_percentage = calculator.find_proportion_threshold(target_percentage)
        
        print(f"El primer número donde la proporción de números bouncy alcanza {target_percentage}% es: {result}")
        print(f"Porcentaje exacto: {exact_percentage:.2f}%")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()