/*
N(1<= N <= 10^5)位同学在海滩参加团建，现在想要建立一个通讯网络供同学们沟通和交流。第i个同学的位置以唯一的(xi,yi)来表示，其中
0 <= xi <= 10^6, 0 <= yi <= 10。通信网络的架设成本为：(xi - xj)^2 + (yi - yj)^2。
若两位同学间有一条链路（节点直接相连或链路由多个子连接构成），那么这两位同学就可以正常通讯。请计算出搭建一套能供所有同学正常通讯的网络所需的最小成本。
*/

#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
struct node{
    ll x,y;
};
node p[100005];
int t,n,m;
struct edge{
    int u,v;
    ll w;
}a[10000015];
bool cmp(const node&l,const node &r)
{
    return l.x<r.x;
}


bool cmp1(const edge &l,const edge &r)
{
    return l.w<r.w;
}
int fa[100005];
int find_fa(int x)
{
    return x==fa[x]?x:fa[x]=find_fa(fa[x]);
}
void find_mst()
{
    sort(a+1,a+m+1,cmp1);
    for(int i=1;i<=n;i++)
        fa[i]=i;
    
    int cnt=0;
    ll ans=0;
    for(int i=1;i<=m;i++)
    {
        int u=a[i].u;
        int v=a[i].v;
        int fu=find_fa(u);
        int fv=find_fa(v);
        if(fu==fv) continue;
        fa[fu]=fv;
        cnt++;
        ans+=a[i].w;
        if(cnt==m-1) break;
    }

    printf("%lld\n",ans);

}




int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%lld%lld",&p[i].x,&p[i].y);

    sort(p+1,p+n+1,cmp);
    edge e;
    
    m=0;
    for(int i=1;i<=n;i++)
    {
        for(int j=i+1;j<=i+100&&j<=n;j++)
        {
            ll w=(p[i].x-p[j].x)*(p[i].x-p[j].x)+(p[i].y-p[j].y)*(p[i].y-p[j].y);
            e.w=w;
            e.u=i;
            e.v=j;
            a[++m]=e;
        }
    }

    find_mst();

    //system("pause");
    return 0;
}