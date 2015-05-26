#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: TexPackageRecognizer.py
# Author:   Lyu Ming <CareF.Lm@gmail.com>


import re

def GetPackagenameInline(TeXLine):
    """This function use regular expression to recognize LaTeX userpackage name"""
    packages = re.findall(r'\\usepackage(?:\[[^\]]*\])?\{([^}]*)\}',TeXLine)
    if packages != None:
        packlist = []
        for packs in packages:
            packlist += packs.split(',')
        return packlist
    else:
        return None

if __name__ == "__main__":
    Sample = '''%!TEX program = xelatex
%!TEX root = ...
\documentclass[12pt,a4paper]{article}%titlepage表示标题单独页
\usepackage{ctex}%ctex套用英文标题格式（建议在英文论文混排中文时使用），ctexcap套用中文格式（等同于\documentclass{ctexart}）
\renewcommand{\figurename}{图}
\renewcommand{\tablename}{表}
\renewcommand{\contentsname}{目录}
%\renewcommand{\thefigure}{\chinese{figure}}%将图片计数改为汉字数字
%\renewcommand{\thetable}{\chinese{table}}%将表格计数改为汉字数字
\usepackage[top=1in,bottom=1in,left=1.5in,right=1.5in]{geometry}%页边距设置：数据来自MS word的默认值
%\usepackage{multicol}页面内多行包
%\usepackage[CJKbookmarks]{hyperref}%给pdf文档添加互动式链接和书签

\usepackage{amsmath,amssymb,esint}%数学公式类宏包；最末为积分符号拓展
\allowdisplaybreaks[0]%允许多行公式间换页，用//*表示不允许换页
%\numberwithin{equation}{section}%公式编号包含章节
\usepackage{bm}%加粗（用于vector）
%\usepackage{textcomp}%符号包，不能用于数学模式，建议不要和SIunits混用
\usepackage[squaren]{SIunits}%科学单位包，可以用于数学模式（为了统一不要和textcomp混用），squaren选项消除和amssymb的冲突
%\usepackage{extarrows}%长箭头, 长v(等号etc.
\usepackage{graphicx}%插图宏包
%\usepackage{picinpar}%图文绕排
\usepackage{array}%表格宏包
%\usepackage{longtable}%长表格宏包
\usepackage{multirow}%多行合并的表格宏包
%\usepackage{booktabs}%表格线宏包

%\usepackage[basic,box,gate,oldgate,ic,optics,physics]{circ}%电路图宏包
%\usepackage[normalem]{ulem}%下划线，删除线等宏包，参数表示不修改\emph{}格式
%\usepackage{mychemistry}%化学宏包，包含mhchem和chemfig
%\usepackage[version=3]{mhchem}%化学宏包，包含mhchem和chemfig
%\usepackage[symbol]{footmisc}%脚注拓展，选项表示用符号做脚注记号
%\usepackage[numbers=left,frame=shadowbox,basicstyle=\ttfamily]{listings}%代码段宏包

%\renewcommand*{\vec}[1]{\bm{#1}}%矢量的格式，这里是加粗
\newcommand{\dif}{\mathrm d}
\newcommand{\diff}{\,\mathrm d}
\newcommand\mi{\mathrm{i}}
\newcommand\e{\mathrm{e}}%定义数学模式中常用的正体字符

\begin{document}
\title{求解 BdG 方程}
\author{吕铭}
\maketitle
\section{理解方程} % (fold)
\label{sec:wtf_is_the_equ}
BdG 方程的表达式:
\begin{equation}\label{equ:bdg}
    \varepsilon \begin{pmatrix}
        u(\vec r) \\ v(\vec r) 
    \end{pmatrix}
    = \begin{pmatrix}
        H + U(\vec r) & \Delta(\vec r) \\
        \Delta^*(\vec r) & -[H^* + U(\vec r)] 
    \end{pmatrix}\begin{pmatrix}
        u(\vec r) \\ v(\vec r)
    \end{pmatrix}\equiv \hat\Omega\begin{pmatrix}
        u \\ v
    \end{pmatrix}
\end{equation}
其中 $H = \left(-\mi\hbar\nabla - eA/c\right)^2/(2m)$ 是体系哈密顿量 (仅考虑磁场, 略去 $U_0$ 势场), 等效势 $U,\Delta$ 定义为: %$\Delta (\vec r)$ 是超导序参量, 定义为: 
\begin{align}
    &U(\vec r) = -V\sum_n\left[|u_n(\vec r)|^2 f_n + |v_n(\vec r)|^2(1 - f_n)\right] \\
    &\Delta(\vec r) = V \sum_n v^*_n(\vec r) u_n(\vec r)(1-2f_n) %= V \sum_n v^*_n(\vec r) u_n(\vec r)\tanh\left(\frac{\beta\varepsilon_n}2\right)
\end{align}
其中 $(u_n, v_n)^T$ 是 $\hat\Omega$ 对应于本征值 $\varepsilon_n$ 的本征函数, $f_n = [\e ^ {\beta(\varepsilon_n - \mu)}+1]^{-1}$ 是 $\varepsilon_n$ 能级上的 Fermi 分布几率. 值得注意的是, $U$ 对于费米面以下的所有状态求和, 对于低温强简并的情形几乎是温度无关的; $V$ 的求和部分对于均匀电子气仅在费米面附近才不为 $0$, 因而强烈地依赖于温度. $u,v$ 满足归一化要求\footnote{这样的归一化要求的实质是 $u$, $v$ 是幺正变换的矩阵元.}:
\begin{equation}
    \int\dif\vec r \left(|u_n(\vec r)|^2 + |v_n(\vec r)|^2\right) = 1
    %\frac 2\Omega\int\dif\vec r\sum_n\left[|u_n(\vec r)|^2 f_n + |v_n(\vec r)|^2(1-f_n)\right] = n_e
\end{equation}
% section wtf_is_the_equ (end)

\end{document}'''

    packagenames = GetPackagenameInline(Sample)
    for name in packagenames:
        print name
    # if packagename != None:
    #     print(packagename)
    # else:
    #     print("No package found")