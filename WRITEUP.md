# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

___
# Criteria 1: Analyze, Choose, and Justify the Resource Option 
- Resource Option Analysis

## Comparing VM vs App Service

### Virtual Machine (VM) Option

#### Costs
- Generally more expensive since you're paying for the whole VM
- Need to factor in costs for OS management and updates
- Resource scaling (CPU, memory, storage) adds significant costs

#### Scalability
- Can scale up or out, but it's not as straightforward
- Requires manual work or custom automation scripts
- Takes longer to spin up new instances

#### Availability
- Azure provides good VM uptime guarantees
- Getting true high availability needs extra setup (load balancers, availability sets)
- More moving parts = more complexity and cost

#### Workflow
- Complete control over your environment
- Can install whatever software you need
- Downside: More management overhead and needs deeper technical knowledge

### App Service Option

#### Costs
- Usually cheaper for web apps like our CMS
- Simple pricing based on service tiers (Basic → Premium)
- Pay for what you use, no infrastructure overhead

#### Scalability
- Built for easy scaling - just slide a slider!
- Automatic scaling based on traffic
- New instances spin up quickly

#### Availability
- Comes with 99.95% uptime guarantee out of the box
- No extra configuration needed
- Azure handles the heavy lifting

#### Workflow
- Much simpler deployment process
- Works great with modern CI/CD pipelines
- Less time managing servers, more time coding

## My Recommendation
I'd go with App Service for this CMS app. It's cheaper, easier to manage, and handles scaling automatically. Since we're building a standard web app, we don't need the extra control that VMs provide. This way, the team can focus on building features rather than managing servers.

___
# Criteria 2: Assess App Changes That Would Change the Decision

If the “Article CMS” application requirements evolve to need more extensive customization, like installing specialized software, modifying OS-level settings, or managing complex networking configurations, a VM may become a more suitable option. Additionally, if there’s a need for stringent compliance or security measures requiring complete control over the environment, the VM option could provide the necessary flexibility.