/*
训练营圆满结束，同学们站在一起合影。
已知第i个同学喜欢的颜色是ai（注：可能有多个同学喜欢同一种颜色）。合影的照片用一个数组表示，bi代表照片第i段的颜色。
对于一个照片的区间而言，只要这个区间存在某同学喜欢的颜色，这个同学就会喜欢这个区间。
现在有q次询问，每次询问一个区间[l,r]有多少个同学喜欢。
*/

#include<bits/stdc++.h>
using namespace std;
const int maxn=2e5+10;
int a[maxn],c[maxn],b[maxn];
struct node{
    int l,r,id;
}s[maxn];
int n,m,o,q,t;
int num[maxn],sum[maxn],ans[maxn];

bool cmp(const node &x,const node &y)
{
    if(x.l/t==y.l/t) return x.r>y.r;
    return x.l<y.l;
}

int main()
{
    memset(a,0,sizeof a);
    memset(b,0,sizeof c);
    memset(c,0,sizeof c);
    memset(num,0,sizeof num);
    memset(sum,0,sizeof sum);

    scanf("%d%d",&n,&m);
    int cnt=0;
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&a[i]);
        b[++cnt]=a[i];
    }
    for(int i=1;i<=m;i++)
    {
        scanf("%d",&c[i]);
        b[++cnt]=c[i];
    }

    sort(b+1,b+cnt+1);
    o=unique(b+1,b+cnt+1)-b-1;

    // cout<<"color num: "<<o<<endl;

    for(int i=1;i<=n;i++){
        a[i]=lower_bound(b+1,b+o+1,a[i])-b;
        num[a[i]]++;
    }

    for(int i=1;i<=m;i++){
        c[i]=lower_bound(b+1,b+o+1,c[i])-b;
    }

    // puts("a");
    // for(int i=1;i<=n;i++){
    //     printf("%d ",a[i]);
    // }
    // puts("");

    // puts("c");
    // for(int i=1;i<=m;i++){
    //     printf("%d ",c[i]);
    // }
    // puts("");


    scanf("%d",&q);
    for(int i=1;i<=q;i++)
    {
        scanf("%d%d",&s[i].l,&s[i].r);
        if(s[i].r<s[i].l) swap(s[i].l,s[i].r);
        s[i].id=i;
    }
    
    t=(int)(sqrt(1.0*m)+0.5);

    sort(s+1,s+q+1,cmp);
    int l=0,r=0,res=0;
    for(int i=1;i<=q;i++)
    {
        while(r<s[i].r)
        {
            r++;
            sum[c[r]]++;
            if(sum[c[r]]==1){
                res+=num[c[r]];
            }
        }

        while(r>s[i].r)
        {
            sum[c[r]]--;
            if(sum[c[r]]==0){
                res-=num[c[r]];
            }
            r--;
        }

        while(l>s[i].l)
        {
            l--;
            sum[c[l]]++;
            if(sum[c[l]]==1){
                res+=num[c[l]];
            }
        }

        while(l<s[i].l)
        {
            sum[c[l]]--;
            if(sum[c[l]]==0){
                res-=num[c[l]];
            }
            l++;
        }
        
        ans[s[i].id]=res;
    }
    for(int i=1;i<=q;i++)
        printf("%d\n",ans[i]);

    //system("pause");
    return 0;
}