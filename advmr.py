a
    �Z�_�  �                   @   sX  d dl mZ d dlmZmZmZ d dlm	Z	 d dl
mZmZ d dlmZ d dlmZ d dlmZmZ dZd	Zeee� d
Zdd� Zed� e�  e	d�r�e	d�r�edd�Zedd�Ze�� Ze�� Ze��  e��  nVe d�Ze d�Zedd�Zedd�Ze�!e� e�!e� e��  e��  ed� e�  dd� Z"dd� Z#dd� Z$e%dk�rTe$�  dS )�    )�system)�stdout�argv�exit)�exists)�uniform�randint)�sleep)�date)�get�postu�   

÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷


u^   
	± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± 

z/-\|c                  C   s8   d} d}t d|  � t d| � td� t d|  � d S )Nz_ '
############################################################################
	 ' | lolcat
	 a#   '
 	_|      _|  _|_|_|                        _|
 	_|_|  _|_|  _|    _|        _|_|_|    _|_|_|  _|      _|
 	_|  _|  _|  _|_|_|        _|    _|  _|    _|  _|      _|
 	_|      _|  _|    _|      _|    _|  _|    _|    _|  _|
 	_|      _|  _|    _|        _|_|_|    _|_|_|      _|
	' | lolcatZechouF   [1;30;40m 	 © script  by  cyco      [  https://github.com/sl-cyco  ])�shell�print)Zname_bar�name� r   �advmr.py�banner   s    r   �clear�url�auth�rz#

saved url not found..enter Url : z6
saved authorization not found..enter Authorization : �wc                  C   s    t ddddd�} td| d�}|S )N�
2018.3.0f2�megarun.dialog.lk�
Keep-Alive�gzip��Authorization�X-Unity-Version�Host�
Connection�Accept-Encodingz2https://megarun.dialog.lk/api/v2/reviev/drawpoints�Zheaders)r   r   ��header�resr   r   r   �
drawpoints@   s    r&   c                  C   s"   t dddddd�} td| d�}|S )	Nr   z!application/x-www-form-urlencodedr   r   r   )r   r   zContent-Typer   r    r!   z%https://megarun.dialog.lk/api/v2/playr"   )r   r   r#   r   r   r   �playH   s    r'   c                  C   s�  zt t� �dkrtd� W n ts&ty8   td� Y n0 td�D ]D} z"t t� �dkr`td� nW  q�W qB   td� td� Y qB0 qBt	d�r�t
dd�}|�� }|��  |t t�� �kr�td� n(t
dd	�}|�t t�� �� |��  d
}d}d}d}d}d}d}d}	d}
tddddd�}d}t	d��r^t
dd�}|D ]}|�� �r8|t|�7 }�q8|��  || | | dk�r�td� �q�|t t�� �k�r�|dk�r�td� �q�tdd�}td� td�D ]8}ttt��D ]$}t|d � t�dt|  � �qҐq�td� t�  ztt|d�}|d7 }W n" t�s2t�yD   td� Y n0 t |�dk�r^|	d7 }	n�t |�dk�r|jd k�r�|d!7 }|d7 }nd|jd"k�r�|d#7 }|d7 }nF|jd$k�r�|d7 }|d7 }n(|jd%k�r�|d&7 }|d7 }n
t|j� t
dd'�}|�d(� |��  n0t |�dk�s&|jd)k�r4td*� �q�n|
d7 }
td+t td,d-�� d. t � td/t |� � td0t td,d-�� d. t � td1t |	� � |
dk�r�td0t td,d-�� d. t � td2t td,d-�� d3 t |
� � |dk�r,td0t td,d-�� d. t � td2t td,d-�� d4 t |� � |dk�rvtd0t td,d-�� d. t � td2t td,d-�� d5 t |� � |dk�r�td0t td,d-�� d. t � td2t td,d-�� d6 t |� � |dk�r
td0t td,d-�� d. t � td2t td,d-�� d7 t |� � || | | dk�r�td0t td,d-�� d. t � td2t td,d-�� d8 t || | | � � td0t td,d-�� d. t � td2t td,d-�� d9 t |
 � d: � td0t td,d-�� d. t � �qd S );Nz<Response [401]>z'

[1;31;40m [#] ...user blocked... [#]u(   
[0;31;40m[¿] ...no internet... [?] 

�   z5
[0;31;40mSomthing wrong..retrying in 5 seconds...

Ztdyr   zrm tdy mg_countr   z0.0r   r   r   r   r   r   Zmg_count�   z*
[1;36;40m Daily message limit reached...z,
[0;36;40m Daily message limit reached...

�F   �   �
�d   i�  zrunning... r   r"   �   z<Response [204]>z<Response [200]>z{"type":"data","size":10}�
   z{"type":"data","size":50}�2   z{"type":"data","size":100}z{"type":"data","size":200}��   �az1
z.{"status":429,"message":"Rate limit exceeded"}z&
[1;31;40m [#] ...user blocked... [#]z

[0;�    �%   z;40mz	All requests 			: z[0;z	No data responses 		: z[1;z;40m	Wrong requests 			: z;40m	10mb messages 			: z;40m	50mb messages 			: z;40m	100mb messages 			: z;40m	200mb messages 			: z;40m	Total messages 			: z ;40m	Total from this session 	: Zmb)�strr&   �prnt_ext�ConnectionErrorZNewConnectionError�ranger'   r   r	   r   �open�read�closer
   Ztodayr   �writer   �	isnumeric�intr   �len�br   r   r   r   �textr   �bar�cut)Zc_countZtdy_contentZdayZall_reqZd10Zd50Zd100Zd200Zttl_dtZno_dtZwrng_reqr$   Zmg_cntZmg_cnt_contentZmgZrnd_time�i�or%   r   r   r   �mainO   s�    


















"
"
"
"
".(rF   �__main__N)&�osr   r   �sysr   r   r   r6   �os.pathr   Zrandomr   r   �timer	   Zdatetimer
   Zrequestsr   r   rB   rC   r   r@   r   r9   Zurl_contentZauth_contentr:   r   r   r;   �inputr<   r&   r'   rF   �__name__r   r   r   r   �<module>   sD   







 
