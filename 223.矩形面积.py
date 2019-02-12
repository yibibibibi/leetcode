class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area_1 = (C-A) * (D-B)
        area_2 = (G-E) * (H-F)
        acrossh = min(D,H)
        acrossl = max(B,F)
        verticall = max(A,E)
        verticalr = min(C,G)
        if acrossh < acrossl or verticall > verticalr:
            return area_1 + area_2
        return area_1 + area_2 - (acrossh - acrossl)*(verticalr - verticall)
