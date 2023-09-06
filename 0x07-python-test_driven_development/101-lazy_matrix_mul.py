#!/usr/bin/python3
"""Defines a matrix mul using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Returns the m_a*m_b


    Args:
        m_a (list of lists of ints/floats): matrix a
        m_b (list of lists of ints/floats): matrix b
    """

    return (np.matmul(m_a, m_b))
