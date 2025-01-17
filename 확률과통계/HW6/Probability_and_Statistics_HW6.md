##  확률과통계 과제 2-3

이공계생을 위한 확률과 통계 - 강혜정 저

glee1228@naver.com

디지털콘텐츠학과 13 이동훈



1. (P363, 2번) 크기가 9인 (소)표본으로부터 모평균 $$\mu $$ 에 대한 $$95\%$$ 신뢰구간이 $$[41,47]$$ 이
   다.
   (a) 표본평균 $$\bar{x} $$ 과 표본표준편차 $$s$$ 를 구하여라.
   $$
   \bar{x}=\frac{41+47}{2}=44\\
   e=3=t_{0.025}(8)\times\frac{s}{3}이므로,\\
   s=\frac{9}{2.306}=3.903
   $$
   

   (b) 모평균 $$ \mu $$ 에 대한 90% 신뢰구간을 구하여라.
   $$
   \bar{x}\pm t_{0.05}(8)\frac{s}{3}= 44\pm 1.86 = [ 42.14, 45.86]
   $$
   

   도움말: (a) 일반적으로 신뢰수준 $$100(1-\alpha)\% $$ 의 신뢰구간은
   $$
   \left[\bar{x}-t_{a/2}\frac{s}{\sqrt{n}},\bar{x}+t_{a/2}\frac{s}{\sqrt{n}} \right]
   $$
   

   이다. 따라서 $$t_{a/2}(n-1)=t_{0.025}(8)=2.306$$ (P523, t-분포표 참고)
   $$
   \left[\bar{x}-t_{0.025}\frac{s}{\sqrt{9}},\bar{x}+t_{0.025}\frac{s}{\sqrt{9}} \right]=[41,47]
   $$
   

   이 사실로부터 표본평균의 측정값 $$\bar{x}$$ 를 구할 수 있고, 오차의 한계 $$e=3 $$ 이므로 표본표준편차
   $$s$$ 를 구할 수 있다.
   (b) $$t_{a/2}(n-1)=t_{0.05}(S)=?$$



2. (P364, 5번 변형) 표본의 크기가 16일 때 표본평균이  $$\bar{X} $$ , 표본표준편차가 $$S$$ 이다. 모평
   균 $$ \mu $$ 에 대한 신뢰구간이 $$\left[\bar{X}-0.6505S,\bar{X}+0.6505S\right]$$ 일 때 신뢰수준은 얼마인가?
   $$
   e=t_{\alpha/2}(15)\frac{S}{\sqrt{16}}=0.6505S이므로,\\
   t_{\alpha/2}(15)=2.602,\ P(|T|\le2.602)=0.98이므로\ 신뢰수준은\ 98\%
   $$
   

   

   도움말: 일반적으로 신뢰수준 $$100(1-\alpha)\%$$ 의 신뢰구간은
   $$
   \left[\bar{X}-t_{a/2}\frac{S}{\sqrt{n}},\bar{X}+t_{a/2}\frac{S}{\sqrt{n}}\right]
   $$
   

   이다. 따라서 $$e=t_{a/2}\frac{S}{\sqrt{n}}$$ 이므로 $$t_{a/2}(15)=?$$ 을 구할 수 있으며,
   $$
   P(|T|\le t_{a/2}(12))=?
   $$
    (t-분포표 참고)



3. (P365, 19번) 어떤 제약회사는 자사에서 만드는 비타민은 열과 습기에 노출되었을 때 10일
   이 지나도 효과에 변화가 없다고 주장한다. 이 주장을 검정하기 위하여 임의로 10개의 비타민
   알약의 효능을 검사하였다.
   (a) 효능 평균유지시간(일) $$ \mu $$ 에 대한 가설을 설정하여라.
   $$
   현재\ 상태를 나타내는 \ 귀무가설은\\ H_0:\ '제약회사에서\ 만든\ 비타민은\ 열과\ 습기에\ 노출되었을\ 때\ 10일이\ 지나면\ 효과에\ 변화가\ 있다.'\\
   H_0:\mu=10\\
   대립가설은\\
   H_1:\ '제약회사에서\ 만든\ 비타민은\ 열과\ 습기에\ 노출되었을\ 때\ 10일이\ 지나도\ 효과에\ 변화가\ 없다.'\\
   H_1:\mu>10
   $$
   

   (b) 검정통계량의 분포를 정하고 유의수준  $$\alpha $$ 에서 가설에 대한 기각역을 결정하여라.
   $$
   검정통계량\ T=\frac{\bar{X}-10}{S/\sqrt{10}}\sim t(9),\\
   기각역\ t_0>t_\alpha(9)
   $$
   

   (c) 유의수준 $$ \alpha=0.05 $$  에서 가설검정의 실시하여라.
   $$
   \bar{x}= \frac{1}{10}(11.3+10.9+10.9+9.4+8.9+10.6+10.7+10.1+10.2+11.5)\\
   = 10.45\\
   s^2= \frac{1}{9}((11.3-10.45)^2+(10.9-10.45)^2+(10.9-10.45)^2+(9.4-10.45)^2\\
   +(8.9-10.45)^2+(10.6-10.45)^2+(10.7-10.45)^2+(10.1-10.45)^2\\
   +(10.2-10.45)^2+(11.5-10.45)^2)\\
   = \frac{1}{9}(0.7225+0.2025+0.2025+1.1025+2.4025+0.0225\\
   +0.0625+0.1225+0.0625+1.1025)\\
   =0.667\\
   s=0.82\\
   t_0=\frac{\bar{x}-\mu_0}{S/\sqrt{n}}=\frac{10.45-10}{0.82/\sqrt{10}}=1.74\\
   t_{0.05}(9)=1.833이므로,\\
   귀무가설을\ 기각할\ 수\ 없다.
   $$
   

   도움말: (a) 10개의 소표본에 대한 표본평균 측정값 $$\bar{x}=10.45,\ s=0.82$$ 라고 하자.
   가설검정(단측검정)
   $$
   H_0:\mu=10,\ H_1:\mu>10
   $$
   


   (b) 검정통계량 $$T=\frac{\bar{X}-\mu_0}{\frac{S}{\sqrt{n}}}$$ 은 자유도 10-1=9인 t-분포를 따른다. 따라서 검정통계량의 값 
   $$
   t_0 = \frac{\bar{x}-\mu_0}{\frac{s}{\sqrt{n}}}>t_\alpha(9)
   $$
   

    이면 귀무가설을 기각한다.
   (c) $$t_0=\frac{\bar{x}-\mu_0}{s/\sqrt{n}}=?,\ t_\alpha(9)=t_{0.05}(9)=?$$