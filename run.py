a
    !��_�	  �                   @   s�  d dl mZmZmZmZmZ d dlmZ d dl	m
Z d dlmZ d dlmZmZ d dlmZ ed�rled� d	d
� Zed� e�  edeedd�� d � ed� ed� ed� zeed��ZW q�W q� ey�   ed� Y q�0 q�ed� e�  edk�r�ed� dZg Ze� D ]LZe�� �redeedd�� d ee� d e � ed7 Ze�e� �qe�sred� n,eed��Z eee d  �Z!ede! d � edk�reedeedd�� d ��Z"eee"�� edee"�d  � eee"�� ed��red!� ned"� ed#k�r�ed� dZg Ze� D ]LZe�� �r,edeedd�� d ee� d e � ed7 Ze�e� �q,eed$��Z eee d  �Z!ee!� ee!��s�edeedd�� d% � ned&� ed'k�r�ed(� d)S )*�    )�system�listdir�mkdir�chdir�getcwd)�exists)�	getoutput)�randint)�copyfile�rmtree)�exitZadvmrz8

		[1;31;40mFirstly install tool  [ sh install.sh ]


c                  C   s8   d} d}t d|  � t d| � td� t d|  � d S )Nz_ '
############################################################################
	 ' | lolcat
	 a#   '
 	_|      _|  _|_|_|                        _|
 	_|_|  _|_|  _|    _|        _|_|_|    _|_|_|  _|      _|
 	_|  _|  _|  _|_|_|        _|    _|  _|    _|  _|      _|
 	_|      _|  _|    _|      _|    _|  _|    _|    _|  _|
 	_|      _|  _|    _|        _|_|_|    _|_|_|      _|
	' | lolcatZechouF   [1;30;40m 	 © script  by  cyco      [  https://github.com/sl-cyco  ])�shell�print)Zname_bar�name� r   �run.py�banner   s    r   �clearz[0;�    �$   u   ;40m

1 ↬  run MR  u   
2 ↬  Add new sim  u   
3 ↬  Remove a sim  u   
4 ↬  Uninstall  
z
Selection  : z[0;31;40m...invalid... �   z

z;40m
u    ↬  z1
[1;31;40mSIM list is empty..Firstly add a sim 
z
Select a number for run  : zcd z ; python advmr.py�   z;40m

Enter mobile number :  zadvmr.pyz	/advmr.pyz[0;32;40mcompleted... z[0;31;40m...somthing wrong... �   z
Select a number for remove  : z;40mcompleted... z[0;31;40m...somthing wrong...�   zsh uninstall.shN)#�osr   r   r   r   r   r   �os.pathr   �
subprocessr   �getZrandomr	   Zshutilr
   r   �sysr   Zprnt_extr   r   �str�int�inputZchoice�
ValueErrorZpnumZplistZpn�	isnumeric�appendZ	slcttd_pn�pathZmobr   r   r   r   �<module>   st   


*






*

